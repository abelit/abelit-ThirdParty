<template>
  <v-container>
    <v-row>
      <v-col>
        <v-alert dense type="info"
          >Which is better, state A or state B?</v-alert
        >
      </v-col>
    </v-row>
    <v-row v-for="(item, index) in listTemp" :key="item.id">
      <v-col cols="12" v-if="index == itemOrder">
        <v-row align="center" justify="center">
          <v-col cols="4">
            <v-card
              style="height:200px"
              class="pa-3"
              :class="answer == item.answer ? 'primary' : ''"
              v-model="answer"
              @click="chooseAnswer(item.answer)"
            >
              <h3>{{ item[0].answer }}{{ item[0].name }}</h3>
              <p>{{ item[0].source_text }}</p>
            </v-card>
          </v-col>
          <v-col cols="4">
            <v-card
              style="height:200px"
              class="pa-3"
              :class="answer == item.answer ? 'primary' : ''"
              v-model="answer"
              @click="chooseAnswer(item.answer)"
            >
              <h3>{{ item[1].answer }}{{ item[1].name }}</h3>
              <p>{{ item[1].source_text }}</p>
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
    answer: ""
  }),
  created() {
    this.getdceQuestion();

    //console.log(this.getdceQuestion());
  },
  mounted() {
    //console.log(this.dceQuestion);
  },
  computed: {
    ...mapState(["userInfo"]),
    listTemp: function() {
      var list = this.dceQuestion;
      var arrTemp = [];
      var index = 0;
      for (var i = 0; i < list.length; i++) {
        index = parseInt(i / 2);
        if (arrTemp.length <= index) {
          arrTemp.push([]);
        }
        arrTemp[index].push(list[i]);
      }
      console.log(arrTemp);
      return arrTemp;
    }
  },
  methods: {
    nextBtn() {
      this.itemOrder++;
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
