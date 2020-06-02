import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const state = {
  examType: JSON.parse(localStorage.getItem("examType")) || [],
  examStart: localStorage.getItem("examStart") || false,
  userInfo: JSON.parse(localStorage.getItem("userInfo")) || [],
  blocks: [],
  allAnswer: JSON.parse(localStorage.getItem("allAnswer")) || [],
  qVersion: localStorage.getItem("qVersion") || "",
  language: localStorage.getItem("language") || "zh_cn",
  eqLangLabels: JSON.parse(localStorage.getItem("eqLangLabels")) || [],
  nstpPage: localStorage.getItem("nstpPage") || 1,
  nstpReset: 0
};

const actions = {
  setExamType({
    commit
  }, obj) {
    commit("setExamType", obj);
  },
  setExamStart({
    commit
  }, value) {
    commit("setExamStart", value);
  },
  setUserInfo({
    commit
  }, obj) {
    commit("setUserInfo", obj);
  },
  setBlocks({
    commit
  }, obj) {
    commit("setBlocks", obj);
  },
  setAllAnswer({
    commit
  }, obj) {
    commit("setAllAnswer", obj);
  },
  setQuestionVersion({
    commit
  }, obj) {
    commit("setQuestionVersion", obj);
  },
  setLanguage({
    commit
  }, value) {
    commit("setLanguage", value);
  },
  setEqLangLabel({
    commit
  }, obj) {
    commit("setEqLangLabel", obj);
  },
  setNstpPage({
    commit
  }, value) {
    commit("setNstpPage", value);
  },
  setNstpReset({
    commit
  }, obj) {
    commit("setNstpReset", obj);
  }
};

const mutations = {
  setExamType: (state, obj) => {
    state.examType = obj;
    localStorage.setItem("examType", JSON.stringify(obj));
  },
  setExamStart: (state, value) => {
    state.examStart = value;
    localStorage.setItem("examStart", value);
  },
  setUserInfo: (state, obj) => {
    state.userInfo = obj;
    localStorage.setItem("userInfo", JSON.stringify(obj));
  },
  setBlocks: (state, obj) => {
    state.blocks = obj;
    localStorage.setItem("blocks", JSON.stringify(obj));
  },
  setAllAnswer: (state, obj) => {
    state.allAnswer = obj;
    localStorage.setItem("allAnswer", JSON.stringify(obj));
  },
  setQuestionVersion: (state, value) => {
    state.qVersion = value;
    localStorage.setItem("qVersion", value);
  },
  setLanguage: (state, value) => {
    state.language = value;
    localStorage.setItem("language", value);
  },
  setEqLangLabel: (state, obj) => {
    state.eqLangLabels = obj;
    localStorage.setItem("eqLangLabels", JSON.stringify(obj));
  },
  setNstpPage: (state, value) => {
    state.nstpPage = value;
    localStorage.setItem("nstpPage", value);
  },
  setNstpReset: (state, obj) => {
    if (obj.reset == 1) {
      state.nstpReset = obj.value;
    } else {
      state.nstpReset += obj.value;
    }
    localStorage.setItem("nstpReset", state.nstpReset);
  },
};

export default new Vuex.Store({
  state,
  mutations,
  actions
});