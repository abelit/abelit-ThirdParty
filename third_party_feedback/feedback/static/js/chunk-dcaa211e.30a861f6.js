(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-dcaa211e"],{ae42:function(e,t,r){},bea4:function(e,t,r){"use strict";r.r(t);var i=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("v-container",[r("v-card",[r("v-card-title",{staticClass:"display-1"},[e._v(e._s(e.eqLangLabels[e.$vuetify.lang.current].T4))]),r("v-card-text",[r("v-row",{staticClass:"mt-12",attrs:{justify:"center"}},[r("v-col",{attrs:{cols:"2",xs:"4"}},[r("v-subheader",{staticClass:"eq-userinfo"},[e._v(e._s(e.eqLangLabels[e.$vuetify.lang.current].T5))])],1),r("v-col",{attrs:{cols:"4",xs:"4"}},[r("v-select",{attrs:{items:e.interviewerList,"item-text":"name","item-value":"id",label:"- "+e.eqLangLabels[e.$vuetify.lang.current].interviewer+" -",outlined:""},model:{value:e.interviewer,callback:function(t){e.interviewer=t},expression:"interviewer"}})],1)],1),r("v-row",{staticClass:"mt-12",attrs:{justify:"center"}},[r("v-col",{attrs:{cols:"2"}},[r("v-subheader",{staticClass:"eq-userinfo"},[e._v(e._s(e.eqLangLabels[e.$vuetify.lang.current].T6))])],1),r("v-col",{attrs:{cols:"4"}},[r("v-text-field",{attrs:{label:"- "+e.eqLangLabels[e.$vuetify.lang.current].participant+" -",outlined:""},model:{value:e.participant,callback:function(t){e.participant=t},expression:"participant"}})],1)],1),"A"!=e.blocks[0]?r("v-row",{staticClass:"mt-12",attrs:{justify:"center"}},[r("v-col",{attrs:{cols:"2"}},[r("v-subheader",{staticClass:"eq-userinfo"},[e._v(e._s(e.eqLangLabels[e.$vuetify.lang.current].T7))])],1),r("v-col",{attrs:{cols:"4"}},[r("v-select",{attrs:{items:e.blocks,label:"- "+e.eqLangLabels[e.$vuetify.lang.current].block+" -",outlined:""},model:{value:e.blockQuestion,callback:function(t){e.blockQuestion=t},expression:"blockQuestion"}})],1)],1):e._e()],1),r("v-card-actions",[r("v-spacer"),r("v-btn",{staticClass:"mt-12",attrs:{color:"#0094ff","x-large":"",height:"72",width:"200",dark:""},on:{click:function(t){return e.saveUserInfo()}}},[e._v(e._s(e.eqLangLabels[e.$vuetify.lang.current].continue))]),r("v-spacer")],1)],1)],1)},n=[],s=r("9660");function a(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);t&&(i=i.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,i)}return r}function c(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?a(Object(r),!0).forEach((function(t){o(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):a(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function o(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}var l={name:"EqUserInfo",data:function(){return{interviewerList:[],blockQuestions:[],interviewer:"",participant:"",blockQuestion:"",itemText:"cnname"}},methods:{saveUserInfo:function(){var e=this;"A"==this.blocks[0]&&(this.blockQuestion="A");var t={interviewer:this.interviewer,participant:this.participant,blockQuestion:this.blockQuestion};if(!(this.interviewer&&this.participant&&this.blockQuestion)&&"A"!=this.blocks[0]||(!this.interviewer||!this.participant)&&"A"==this.blocks[0])return alert("信息填写不完整"),!1;this.$store.dispatch("setUserInfo",t).then((function(){e.$router.push({path:"/eq/tip"})}))},getInterviewer:function(){var e=this;this.$axios.get("/api/interviewer",{params:{version:this.qVersion}}).then((function(t){e.interviewerList=t.data}))}},mounted:function(){this.getInterviewer(),console.log(this.eqLangLabels)},computed:c({},Object(s["b"])(["blocks","eqLangLabels","qVersion"]))},u=l,v=(r("df24"),r("e90a")),b=Object(v["a"])(u,i,n,!1,null,null,null);t["default"]=b.exports},df24:function(e,t,r){"use strict";var i=r("ae42"),n=r.n(i);n.a}}]);
//# sourceMappingURL=chunk-dcaa211e.30a861f6.js.map