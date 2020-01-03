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
            class="ma-3 pa-6 text-center display-1"
            color="#036f90"
            outlined
            width="240"
            height="120"
            dark
            @click="saveExamType(item)"
            >{{ item.name }}</v-card
          >
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import questiontype from "@/assets/data/questiontype.json";
export default {

  data: () => ({
    questionType: questiontype
  }),
  methods: {
    saveExamType(value) {
      console.log(value);
      this.getQuestionNum(value.id);
      this.$store.dispatch("setExamType", value).then(() => {
        // 跳转到指定页面
        this.$router.push({ path: "/eq" });
      });
    },
    getQuestionNum(id) {
      this.$axios
        .get("/api/question/blocks", {
          params: { type: id }
        })
        .then(res => {
          console.log(res.data);
          this.$store.dispatch("setBlocks", res.data);
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>
