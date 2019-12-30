import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const state = {
  examType: JSON.parse(localStorage.getItem("examType")) || "",
  examStart: localStorage.getItem("examStart") || false,
  userInfo: JSON.parse(localStorage.getItem("userInfo")) || "",
  blocks: ""
};

const actions = {
  setExamType({ commit }, obj) {
    commit("setExamType", obj);
  },
  setExamStart({ commit }, value) {
    commit("setExamStart", value);
  },
  setUserInfo({ commit }, obj) {
    commit("setUserInfo", obj);
  },
  setBlocks({ commit }, obj) {
    commit("setBlocks", obj);
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
  }
};

export default new Vuex.Store({
  state,
  mutations,
  actions
});
