/* Daver – statický runtime pro .dc.html šablony (export z canvasu).
   Šablony jsou předem převedené na JSON strom (export.py), vykreslení přes Preact. */
(function () {
  'use strict';
  var P = window.preact, h = P.h, render = P.render, Component = P.Component, Fragment = P.Fragment;
  var COMPS = window.__DC || {};
  var cache = {};

  function look(path, ctx) {
    path = path.trim();
    if (path === 'true') return true;
    if (path === 'false') return false;
    if (path === 'null') return null;
    if (/^-?\d+(\.\d+)?$/.test(path)) return +path;
    if (/^(['"]).*\1$/.test(path)) return path.slice(1, -1);
    var parts = path.split('.'), v = ctx[parts[0]];
    for (var i = 1; i < parts.length && v != null; i++) v = v[parts[i]];
    return v;
  }
  var WHOLE = /^\s*\{\{([^}]*)\}\}\s*$/;
  function val(s, ctx) {
    if (s == null) return s;
    var m = s.match(WHOLE);
    if (m) return look(m[1], ctx);
    if (s.indexOf('{{') < 0) return s;
    return s.replace(/\{\{([^}]*)\}\}/g, function (_, p) { var v = look(p, ctx); return v == null ? '' : String(v); });
  }
  function camel(k) { return k.replace(/-([a-z])/g, function (_, c) { return c.toUpperCase(); }); }
  var BOOL = { disabled: 1, checked: 1, selected: 1, readonly: 1, required: 1, hidden: 1, multiple: 1, open: 1 };

  function kids(nodes, ctx, out) {
    out = out || [];
    for (var i = 0; i < nodes.length; i++) {
      var r = node(nodes[i], ctx);
      if (Array.isArray(r)) { for (var j = 0; j < r.length; j++) out.push(r[j]); }
      else if (r != null && r !== false) out.push(r);
    }
    return out;
  }

  function node(n, ctx) {
    if (typeof n === 'string') {
      if (n.indexOf('{{') < 0) return n;
      var parts = [], last = 0;
      n.replace(/\{\{([^}]*)\}\}/g, function (m, p, i) {
        if (i > last) parts.push(n.slice(last, i));
        var v = look(p, ctx);
        if (v != null && v !== false) parts.push(String(v));
        last = i + m.length;
      });
      if (last < n.length) parts.push(n.slice(last));
      return parts;
    }
    var tag = n[0], attrs = n[1], ch = n[2], A = {}, k, v, i;
    for (i = 0; i < attrs.length; i++) A[attrs[i][0]] = attrs[i][1];
    if (tag === 'helmet') return null;
    if (tag === 'sc-if') return val(A.value, ctx) ? kids(ch, ctx) : null;
    if (tag === 'sc-for') {
      var list = val(A.list, ctx) || [], as = A.as || 'item', res = [];
      for (i = 0; i < list.length; i++) {
        var c = Object.create(ctx); c[as] = list[i]; c.$index = i;
        kids(ch, c, res);
      }
      return res;
    }
    if (tag === 'dc-import') {
      var cp = {};
      for (i = 0; i < attrs.length; i++) {
        k = attrs[i][0];
        if (k === 'name' || k.indexOf('hint-') === 0) continue;
        cp[camel(k)] = val(attrs[i][1], ctx);
      }
      return h(getComp(A.name), cp);
    }
    var props = {};
    for (i = 0; i < attrs.length; i++) {
      k = attrs[i][0];
      if (k.indexOf('hint-') === 0) continue;
      v = val(attrs[i][1], ctx);
      if (/^on[A-Z]/.test(k)) {
        if (typeof v !== 'function') continue;
        var ev = k;
        if (k === 'onChange' && (tag === 'textarea' || (tag === 'input' && !/^(checkbox|radio)$/i.test(A.type || '')))) ev = 'onInput';
        props[ev] = v;
        continue;
      }
      if (k === 'autoFocus') { if (v) props.autofocus = true; continue; }
      if (k === 'tabIndex') k = 'tabindex';
      if (k.indexOf('aria-') === 0) { if (v != null) props[k] = String(v); continue; }
      if (BOOL[k.toLowerCase()]) { props[k.toLowerCase()] = !!(v === '' ? true : v) && v !== 'false'; continue; }
      if (v == null || v === false) continue;
      props[k] = v;
    }
    return h.apply(null, [tag, props].concat(kids(ch, ctx)));
  }

  function getComp(name) {
    if (cache[name]) return cache[name];
    var def = COMPS[name];
    if (!def) { console.warn('[dc] chybí komponenta', name); return function () { return null; }; }
    var tpl = def.tpl;
    function DCLogic(props) { Component.call(this, props); }
    DCLogic.prototype = Object.create(Component.prototype);
    DCLogic.prototype.constructor = DCLogic;
    DCLogic.prototype.render = function () {
      var vals = this.renderVals ? this.renderVals() : {};
      var out = kids(tpl, Object.assign({}, vals));
      return out.length === 1 ? out[0] : h.apply(null, [Fragment, null].concat(out));
    };
    var Cls;
    try { Cls = new Function('DCLogic', def.code + '\n;return Component;')(DCLogic); }
    catch (e) { console.error('[dc] chyba v logice komponenty ' + name, e); Cls = DCLogic; }
    cache[name] = Cls;
    return Cls;
  }

  function boot() {
    var root = document.getElementById('dc-root');
    render(h(getComp(window.__DC_PAGE)), root);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot); else boot();
})();
