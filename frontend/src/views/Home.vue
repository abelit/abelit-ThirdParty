<template>
  <v-container fluid class="pa-0">
    <v-img
      :src="require('@/assets/images/eq5d_bg1.jpg')"
      max-height="40vh"
      :aspect-ratio="16 / 9"
    >
      <v-row align="center" justify="center" style="height: 100%">
        <v-col cols="8">
          <span class="display-3 font-weight-bold" style="color: #014759"
            >Questions?</span
          >
        </v-col>
      </v-row>
    </v-img>
    <v-row class="pt-12">
      <v-col cols="12">
        <v-row align="center" justify="center">
          <v-card
            v-for="item in questionType"
            :key="item.id"
            class="ma-3 text-center display-1 app-card"
            color="#036f90"
            outlined
            width="260"
            height="160"
            dark
            @click="saveExamType(item)"
            >{{ item.name }}</v-card
          >
        </v-row>
      </v-col>
    </v-row>

    <v-row>
      <div class="text-center">
        <v-dialog v-model="dialog" width="500">
          <v-card>
            <v-card-title class="headline grey lighten-2" primary-title>
              请输入验证码
            </v-card-title>

            <v-card-text class="pt-5">
              <v-row>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    label="验证码"
                    outlined
                    dense
                    v-model="vcode"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <verify-code :identifyCode="identifyCode"></verify-code>
                </v-col>
              </v-row>
              <v-row class="pl-3"> 
                <v-alert type="error" v-if="codeErr">
                  验证码错误！
                </v-alert>
              </v-row>
            </v-card-text>

            <v-divider></v-divider>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="primary" text @click="refreshCode">
                刷新
              </v-btn>
              <v-btn color="primary" text @click="startQuestion">
                完成
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </div>
    </v-row>
  </v-container>
</template>

<script>
import questiontype from "@/assets/data/questiontype.json";
import VerifyCode from "@/views/VerifyCode";
export default {
  data: () => ({
    questionType: questiontype,
    eqLabels: [],
    dialog: false,
    identifyCodes: "1234567890",
    identifyCode: "",
    vcode: "", //text框输入的验证码
    examType: "",
    codeErr: false
  }),
  components: {
    VerifyCode,
  },
  methods: {
    saveExamType(value) {
      console.log(value);
      this.refreshCode();
      this.dialog = true;
      this.examType = value;
      // this.getLabel(value.type);
      // this.$store.dispatch("setExamType", value).then(() => {
      //   // 跳转到指定页面
      //   this.$router.push({ path: "/eq" });
      // });
    },
    startQuestion() {
      if (this.identifyCode != this.vcode) {
        // alert("验证码错误！");
        this.codeErr = true;
        return;
      }
      this.dialog = false;
      console.log(this.examType);
      this.getLabel(this.examType.type);
      this.$store.dispatch("setExamType", this.examType).then(() => {
        // 跳转到指定页面
        this.$router.push({ path: "/eq" });
      });
    },
    getLabel(qid) {
      let url = "/api/eqlabel";
      this.$axios
        .get(url, {
          params: {
            questionid: qid,
          },
        })
        .then((res) => {
          let arrData = res.data;
          // let lang = this.$vuetify.lang.current;
          let enObj = new Object();
          let zhObj = new Object();
          let obj = new Object();
          for (let i = 0; i < arrData.length; i++) {
            zhObj[arrData[i].reference_id] = arrData[i].zh_source_text;
            enObj[arrData[i].reference_id] = arrData[i].en_source_text;
          }
          obj.en_us = enObj;
          obj.zh_cn = zhObj;
          this.eqLabels = obj;

          this.$store.dispatch("setEqLangLabel", this.eqLabels);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    randomNum(min, max) {
      return Math.floor(Math.random() * (max - min) + min);
    },

    refreshCode() {
      this.identifyCode = "";
      this.makeCode(this.identifyCodes, 4);
      this.codeErr = false;
    },
    makeCode(o, l) {
      for (let i = 0; i < l; i++) {
        this.identifyCode += this.identifyCodes[
          this.randomNum(0, this.identifyCodes.length)
        ];
      }
      console.log(this.identifyCode);
    },
  },
  created() {
    this.$store.dispatch("setNstpPage", 1);
    this.refreshCode();
  },
  mounted() {
    this.identifyCode = "";
    this.makeCode(this.identifyCodes, 4);
  },
};
</script>

<style lang="scss" scoped>
.app-card {
  display: flex;
  justify-content: center;
  align-items: Center;
}
</style>
