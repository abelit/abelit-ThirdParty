(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d21df88"],{d424:function(e,t,r){"use strict";r.r(t);var n=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("v-container",[r("v-row",[r("v-col",[r("v-card",{attrs:{"min-height":"800","max-height":"1080",justify:"center",align:"center"}},[r("v-card-title",{staticClass:"display-1 pa-12"},[e._v(e._s(e.eqLangLabels[e.$vuetify.lang.current].T10))]),r("v-card-text",{staticClass:"display-1 pa-12 light-green lighten-2",staticStyle:{"margin-top":"100px",width:"500px"},on:{click:e.saveAnswer}},[r("v-progress-circular",{attrs:{size:200,width:e.isCircle?7:0,color:e.isCircle?"primary":"",indeterminate:e.isCircle}},[r("span",{attrs:{color:"success"}},[e._v(e._s(e.eqLangLabels[e.$vuetify.lang.current].T11))])])],1)],1)],1)],1)],1)},i=[],a=r("2f62");function s(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function c(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?s(Object(r),!0).forEach((function(t){l(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):s(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function l(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}var o={data:function(){return{isCircle:!1}},methods:{saveAnswer:function(){var e=this;console.log(this.allAnswer);var t="";1==this.allAnswer[0].questionid?t="/api/answer/dce/addall":2==this.allAnswer[0].questionid?t="/api/answer/tto/addall":3==this.allAnswer[0].questionid?t="/api/answer/ttofeedback/addall":4==this.allAnswer[0].questionid?t="/api/answer/open/addall":alert("后台地址不对"),this.$axios.post(t,this.allAnswer).then((function(t){200==t.status&&(e.isCircle=!0,setTimeout((function(){e.isCircle=!1,e.$router.push({path:"/"})}),5e3))})).catch((function(e){console.log(e)}))}},computed:c({},Object(a["b"])(["allAnswer","eqLangLabels"]))},u=o,p=r("2877"),d=Object(p["a"])(u,n,i,!1,null,null,null);t["default"]=d.exports}}]);
//# sourceMappingURL=chunk-2d21df88.2dc7744d.js.map