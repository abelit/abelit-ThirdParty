(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d21df88"],{d424:function(e,t,r){"use strict";r.r(t);var a=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("v-container",[r("v-row",[r("v-col",[r("v-card",{attrs:{"min-height":"800","max-height":"1080",justify:"center",align:"center"}},[r("v-card-title",{staticClass:"display-1 pa-12"},[e._v(e._s(e.eqLangLabels[e.$vuetify.lang.current].T10))]),r("v-card-text",{staticClass:"display-1 pa-12 light-green lighten-2",staticStyle:{"margin-top":"100px",width:"500px"},attrs:{disabled:""},on:{click:e.saveAnswer}},[r("v-progress-circular",{attrs:{size:200,width:e.isCircle?7:0,color:e.isCircle?"primary":"",indeterminate:e.isCircle}},[r("span",{attrs:{color:"success"}},[e._v(e._s(e.eqLangLabels[e.$vuetify.lang.current].T11))])])],1)],1)],1)],1),r("v-row",[r("v-col",[r("v-snackbar",{model:{value:e.snackbar,callback:function(t){e.snackbar=t},expression:"snackbar"}},[e._v("数据已经成功入库！")])],1)],1)],1)},n=[],s=r("08c1");function i(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,a)}return r}function l(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?i(Object(r),!0).forEach((function(t){c(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):i(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function c(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}var o={data:function(){return{isCircle:!1,isSave:!1,snackbar:!1}},methods:{saveAnswer:function(){var e=this;if(console.log(this.allAnswer),this.isSave)return alert("数据已经提交入库！"),fasle;var t="";1==this.allAnswer[0].questionid?t="/api/answer/dce/addall":2==this.allAnswer[0].questionid?t="/api/answer/tto/addall":3==this.allAnswer[0].questionid?t="/api/answer/ttofeedback/addall":4==this.allAnswer[0].questionid?t="/api/answer/open/addall":5==this.allAnswer[0].questionid?t="/api/answer/nstptto/addall":6==this.allAnswer[0].questionid?t="/api/answer/newtto/addall":alert("后台地址不对"),this.isCircle=!0,this.$axios.post(t,this.allAnswer).then((function(t){200==t.status&&setTimeout((function(){e.isCircle=!1,e.snackbar=!0,setTimeout((function(){e.$router.push({path:"/"})}),2e3)}),1e3),e.isSave=!0})).catch((function(e){console.log(e)}))}},computed:l({},Object(s["b"])(["allAnswer","eqLangLabels"]))},u=o,p=r("5511"),d=Object(p["a"])(u,a,n,!1,null,null,null);t["default"]=d.exports}}]);
//# sourceMappingURL=chunk-2d21df88.4395805b.js.map