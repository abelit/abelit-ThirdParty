<template>
  <v-container>
    <v-row v-for="item in oeqQuestion" :key="item.name">
      <v-col cols="12" v-if="item.name == name">
        <v-row>
          <v-col cols="12">
            <v-card class="mx-auto yellow lighten-4" height="300" dark>
              <v-card-text class="headline font-weight-bold black--text">{{
                item.source_text
              }}</v-card-text>
            </v-card>
          </v-col>
        </v-row>
        <v-row class="mt-10">
          <v-col cols="12">
            <v-textarea
              label="- 请在这里写下你的答案 -"
              outlined
              height="300"
            ></v-textarea>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" align="center" justify="center">
            <v-btn height="72" width="200" color="primary" @click="nextBtn">
              <v-icon>mdi-play</v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
//import dataOeq from "@/assets/data/oeq.json";
export default {
  data: () => ({
    oeqQuestion: [{}],
    step: 0,
    name: ""
  }),
  created() {
    this.getoeqQuestion();
    //this.oeqQuestion = dataOeq;
  },
  mounted() {},
  methods: {
    nextBtn() {
      if (this.step + 1 < this.oeqQuestion.length) {
        this.step++;
        this.name = this.oeqQuestion[this.step].name;
      } else {
        alert("回答完毕");
      }
    },
    getoeqQuestion() {
      this.$axios
        .get("/api/question/open", {
          params: { block: "A" }
        })
        .then(res => {
          //   this.dceQuestion = res.data;
          this.oeqQuestion = res.data;
          this.name = this.oeqQuestion[0].name;
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>
