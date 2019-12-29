<template>
  <v-container>
    <v-row v-for="item in oeqQuestion" :key="item.Name">
      <v-col cols="12" v-if="item.Name == name">
        <v-row>
          <v-col cols="12">
            <v-card class="mx-auto yellow lighten-4" height="300" dark>
              <v-card-text class="headline font-weight-bold black--text"
                >{{ item.Source }}
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
        <v-row class="mt-10">
          <v-col cols="12">
            <v-textarea
              label="- 请在这里写下你的答案 -"
              outlined
              v-model="participant"
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
import dataOeq from "@/assets/data/oeq.json";
export default {
  data: () => ({
    oeqQuestion: [{}],
    step: 0,
    name: ""
  }),
  created() {
    this.oeqQuestion = dataOeq;
  },
  mounted() {
    this.name = this.oeqQuestion[this.step].Name;
    console.log(this.name);
  },
  methods: {
    nextBtn() {
      this.step++;
      this.name = this.oeqQuestion[this.step].Name;
    }
  }
};
</script>
