<template>
  <v-container>
    <v-row>
      <v-col>
        <v-alert dense type="info"
          >Which is better, state A or state B?</v-alert
        >
      </v-col>
    </v-row>
    <v-row v-for="item in dceQuestion" :key="item.id">
      <v-col cols="12" v-if="item.Block == block && item.id == id">
        <v-row align="center" justify="center">
          <v-col cols="4">
            <v-card
              style="height:200px"
              class="pa-3"
              :class="answer == item.AnswerA ? 'primary' : ''"
              v-model="answer"
              @click="chooseAnswer(item.AnswerA)"
            >
              <h3>{{ item.AnswerA }}</h3>
              <p>{{ item.SourceA }}</p>
            </v-card>
          </v-col>
          <v-col cols="4">
            <v-card
              style="height:200px"
              class="pa-3"
              :class="answer == item.AnswerB ? 'primary' : ''"
              v-model="answer"
              @click="chooseAnswer(item.AnswerB)"
            >
              <h3>{{ item.AnswerB }}</h3>
              <p>{{ item.SourceB }}</p>
            </v-card>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" align="center" justify="center">
        <v-btn height="72" width="200" color="primary" @click="nextBtn">
          <v-icon>mdi-play</v-icon>
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
//import dataDce from "@/assets/data/dce.json";
import { mapState } from "vuex";
export default {
  // name: "EqDce",
  // props: ["block1", "startTime"],
  data: () => ({
    dceQuestion: [{}],
    block: 1,
    itemOrder: 0,
    name: "",
    answer: ""
  }),
  created() {
    this.getdceQuestion();

    console.log(this.dceQuestion);
  },
  mounted() {
    //console.log(this.dceQuestion);
  },
  computed: {
    ...mapState(["userInfo"])
  },
  methods: {
    nextBtn() {
      // this.itemOrder++;
      console.log(this.answer);

      // console.log(dataDce[this.itemOrder].Name);
      // if (dataDce[this.itemOrder].Name == undefined) {
      //   alert("ssss");
      // } else {
      //   this.name = dataDce[this.itemOrder].Name;
      // }
    },
    changeCss(item) {
      item.selected = true;
    },
    chooseAnswer(item) {
      this.answer = item;
      console.log(this.answer);
    },
    getdceQuestion() {
      // console.log(this.userInfo.blockQuestion);
      this.$axios
        .get("/api/question/dce", {
          params: { block: this.userInfo.blockQuestion }
        })
        .then(res => {
          this.dceQuestion = res.data;

          // this.currentItem = this.eqTtoQuestions[0].id;
          // console.log(this.dceQuestion);
        })
        .catch(error => {
          console.log(error);
        });
      // console.log(this.eqTtoQuestions);
    }
  }
};
</script>
