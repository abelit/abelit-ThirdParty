<template>
  <v-container fluid class="pa-0">
    <v-img :src="require('@/assets/images/eq5d_bg.jpg')" height="100vh">
      <v-row align="center" justify="center" style="height: 100%">
        <v-col cols="12" class="text-center">
          <v-row>
            <v-col class="mb-12" style="color: white">
              <!-- <span class="display-1">{{ examType.content }}</span> -->
              <span class="display-1">{{ eqLangLabels[$vuetify.lang.current].T1 }}</span>
              <v-spacer class="pb-2"></v-spacer>
              <span class="display-1" dark>{{ new Date().toLocaleString() }}</span>
            </v-col>
          </v-row>
          <v-row justify="center">
            <v-col cols="6" sm="2" class="display-1">
              <v-select
                :items="questionVersions"
                v-model="qVersion"
                item-value="version"
                item-text="version"
                :label="$vuetify.lang.t('$vuetify.form.selectVersion')"
                outlined
                dense
                dark
              ></v-select>
            </v-col>
          </v-row>
          <v-btn color="#0094ff" x-large height="72" dark class="mt-12" @click="startExam()">
            <span class="display-1">{{ eqLangLabels[$vuetify.lang.current].start_survey }}</span>
          </v-btn>
        </v-col>
      </v-row>
    </v-img>
  </v-container>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "EqStartPage",
  data: () => ({
    questionVersions: [],
    qVersion: ""
    // eqLabels: []
  }),
  components: {
    // EqUserInfo
  },
  methods: {
    startExam() {
      this.getQuestionBlock(this.examType.id, this.qVersion);
      this.$store.dispatch("setQuestionVersion", this.qVersion);
      this.$store.dispatch("setExamStart", true).then(() => {
        this.$router.push({ path: "/eq/user" });
      });
    },
    //从后台获取题库版本
    getQuestionVerion() {
      let url = "/api/question/version";
      this.$axios
        .get(url)
        .then(res => {
          // console.log(res.data);
          this.questionVersions = res.data;
          this.qVersion = this.questionVersions[
            this.questionVersions.length - 1
          ].version;
        })
        .catch(err => {
          console.log(err);
        });
    },
    getQuestionBlock(t, v) {
      this.$axios
        .get("/api/question/blocks", {
          params: { type: t, version: v }
        })
        .then(res => {
          // console.log(res.data);
          this.$store.dispatch("setBlocks", res.data);
        })
        .catch(error => {
          console.log(error);
        });
    }
    // getLabel() {
    //   let url = "/api/eqlabel";
    //   this.$axios
    //     .get(url, {
    //       params: {
    //         questionid: this.examType.id
    //       }
    //     })
    //     .then(res => {
    //       let arrData = res.data;
    //       // let lang = this.$vuetify.lang.current;
    //       let enObj = new Object();
    //       let zhObj = new Object();
    //       let obj = new Object();
    //       for (let i = 0; i < arrData.length; i++) {
    //         zhObj[arrData[i].reference_id] = arrData[i].zh_source_text;
    //         enObj[arrData[i].reference_id] = arrData[i].en_source_text;
    //       }
    //       obj.en_us = enObj;
    //       obj.zh_cn = zhObj;
    //       this.eqLabels = obj;

    //       this.$store.dispatch("setEqLangLabel", this.eqLabels);
    //     })
    //     .catch(err => {
    //       console.log(err);
    //     });
    // }
  },
  computed: {
    ...mapState(["examType", "examStart", "eqLangLabels"])
  },
  mounted() {
    this.getQuestionVerion();
    // console.log(this.eqLangLabels);
  },
  created() {
    // this.getLabel();
  }
};
</script>

<style lang="scss">
.v-content__warp {
  height: 100% !important;
}
</style>
