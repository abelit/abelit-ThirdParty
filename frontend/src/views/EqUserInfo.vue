<template>
  <v-container>
    <v-card>
      <v-card-title class="display-1">{{ eqLangLabels[$vuetify.lang.current].T4 }}</v-card-title>
      <v-card-text>
        <v-row justify="center" class="mt-12">
          <v-col cols="2" xs="4">
            <v-subheader class="eq-userinfo">{{ eqLangLabels[$vuetify.lang.current].T5 }}</v-subheader>
          </v-col>
          <v-col cols="4" xs="4">
            <v-select
              :items="interviewerList"
              item-text="name"
              item-value="id"
              :label="'- '+eqLangLabels[$vuetify.lang.current].interviewer+' -'"
              outlined
              v-model="interviewer"
            ></v-select>
          </v-col>
        </v-row>
        <v-row justify="center" class="mt-12">
          <v-col cols="2">
            <v-subheader class="eq-userinfo">{{ eqLangLabels[$vuetify.lang.current].T6 }}</v-subheader>
          </v-col>
          <v-col cols="4">
            <v-text-field
              :label="'- '+eqLangLabels[$vuetify.lang.current].participant+' -'"
              outlined
              v-model="participant"
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row justify="center" class="mt-12" v-if="blocks[0] != 'A'">
          <v-col cols="2">
            <v-subheader class="eq-userinfo">{{ eqLangLabels[$vuetify.lang.current].T7 }}</v-subheader>
          </v-col>
          <v-col cols="4">
            <v-select
              :items="blocks"
              :label="'- '+eqLangLabels[$vuetify.lang.current].block+' -'"
              outlined
              v-model="blockQuestion"
            ></v-select>
          </v-col>
        </v-row>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          color="#0094ff"
          x-large
          height="72"
          width="200"
          dark
          class="mt-12"
          @click="saveUserInfo()"
        >{{eqLangLabels[$vuetify.lang.current].continue}}</v-btn>
        <v-spacer></v-spacer>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "EqUserInfo",
  data: () => ({
    interviewerList: [],
    blockQuestions: [],
    interviewer: "",
    participant: "",
    blockQuestion: "",
    itemText: "cnname"
  }),
  methods: {
    saveUserInfo() {
      if (this.blocks[0] == "A") {
        this.blockQuestion = "A";
      }
      var obj = {
        interviewer: this.interviewer,
        participant: this.participant,
        blockQuestion: this.blockQuestion
      };

      if (
        (!(this.interviewer && this.participant && this.blockQuestion) &&
          this.blocks[0] != "A") ||
        (!(this.interviewer && this.participant) && this.blocks[0] == "A")
      ) {
        alert("信息填写不完整");
        return false;
      }

      this.$store.dispatch("setUserInfo", obj).then(() => {
        // console.log(obj);
        // 跳转到提示路由
        this.$router.push({ path: "/eq/tip" });
      });
    },
    // 从后台获取interviewer
    getInterviewer() {
      this.$axios.get("/api/interviewer",{
         params: {version: this.qVersion }
      }).then(res => {
        this.interviewerList = res.data;
        // console.log(this.interviewerList);
      });
    }
  },
  mounted() {
    this.getInterviewer();
    console.log(this.eqLangLabels);
  },
  computed: {
    ...mapState(["blocks", "eqLangLabels","qVersion"])
  }
};
</script>

<style lang="scss">
.eq-userinfo {
  color: black !important;
  font-size: 16px;
}
</style>
