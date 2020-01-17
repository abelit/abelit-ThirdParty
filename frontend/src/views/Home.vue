<template>
  <v-container fluid class="pa-0">
    <v-img :src="require('@/assets/images/eq5d_bg1.jpg')" max-height="40vh" :aspect-ratio="16 / 9">
      <v-row align="center" justify="center" style="height: 100%">
        <v-col cols="8">
          <span class="display-3 font-weight-bold" style="color: #014759">Questions?</span>
        </v-col>
      </v-row>
    </v-img>
    <v-row class="pt-12">
      <v-col cols="12">
        <v-row align="center" justify="center">
          <v-card
            v-for="item in questionType"
            :key="item.id"
            class="ma-3 pa-6 text-center display-1"
            color="#036f90"
            outlined
            width="240"
            height="120"
            dark
            @click="saveExamType(item)"
          >{{ item.name }}</v-card>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import questiontype from "@/assets/data/questiontype.json";
export default {
  data: () => ({
    questionType: questiontype,
    eqLabels: []
  }),
  methods: {
    saveExamType(value) {
      // console.log(value);
      this.getLabel(value.id);
      this.$store.dispatch("setExamType", value).then(() => {
        // 跳转到指定页面
        this.$router.push({ path: "/eq" });
      });
    },
    getLabel(qid) {
      let url = "/api/eqlabel";
      this.$axios
        .get(url, {
          params: {
            questionid: qid
          }
        })
        .then(res => {
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
        .catch(err => {
          console.log(err);
        });
    }
  }
};
</script>
