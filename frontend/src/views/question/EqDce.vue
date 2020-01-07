<template>
  <v-container v-show="dceQuestion.length > 1">
    <v-row>
      <v-col>
        <v-alert dense type="info"
          >Which is better, state A or state B?</v-alert
        >
      </v-col>
    </v-row>
    <v-row v-for="item in dceQuestion" :key="item.id">
      <v-col cols="6" v-if="item.name == name">
        <v-card
          style="height:300px;font-size:1.5em"
          class="pa-3"
          v-model="selectedAnswer"
          :class="item.answerA == selectedAnswer ? 'primary' : ''"
          @click="chooseAnswer(item.answerA)"
        >
          <h2>{{ item.answerA }}</h2>
          <div v-if="randNum == 1">
            <div v-for="msg in item.sourceTextA.split('*')" :key="msg.key">
              <li v-if="msg != ''">
                <span>{{ msg }}</span>
              </li>
            </div>
          </div>
          <div v-else>
            <div v-for="msg in item.sourceTextB.split('*')" :key="msg.key">
              <li v-if="msg != ''">
                <span>{{ msg }}</span>
              </li>
            </div>
          </div>
        </v-card>
      </v-col>
      <v-col cols="6" v-if="item.name == name">
        <v-card
          style="height:300px;font-size:1.5em"
          class="pa-3"
          v-model="selectedAnswer"
          :class="item.answerB == selectedAnswer ? 'primary' : ''"
          @click="chooseAnswer(item.answerB)"
        >
          <h2>{{ item.answerB }}</h2>
          <div v-if="randNum == 1">
            <div v-for="msg in item.sourceTextB.split('*')" :key="msg.key">
              <li v-if="msg != ''">
                <span>{{ msg }}</span>
              </li>
            </div>
          </div>
          <div v-else>
            <div v-for="msg in item.sourceTextA.split('*')" :key="msg.key">
              <li v-if="msg != ''">
                <span>{{ msg }}</span>
              </li>
            </div>
          </div>
        </v-card>
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
  data: () => ({
    dceQuestion: [],
    block: 1,
    itemOrder: [],
    name: "",
    selectedAnswer: "",
    dceAnswers: [],
    dceReversal: "NORMAL",
    randNum: 1
  }),
  created() {
    this.getdceQuestion();
    this.randNum = this.randomNum(1, 2);
    console.log(this.randNum);
  },
  mounted() {},
  computed: {
    ...mapState(["userInfo", "examType"])
  },
  methods: {
    nextBtn() {
      if (!this.selectedAnswer) {
        alert("请选择您的答案！");
        return false;
      }

      if (this.itemOrder.indexOf(this.name) + 1 >= this.itemOrder.length) {
        alert("回答完毕！");
        this.$store.dispatch("setAllAnswer", this.dceAnswers);
        this.$router.push({ path: "/eq/end" });
      }

      if (this.randNum == 1) {
        this.dceReversal = "NORMAL";
      } else {
        this.dceReversal = "NONORMAL";
      }

      var answerObj = {
        questionid: this.examType.id,
        participant: this.userInfo.participant,
        interviewer: this.userInfo.interviewer,
        item: this.name,
        position_of_item: this.itemOrder.indexOf(this.name) + 1,
        selected_state: this.selectedAnswer,
        dce_reversal: this.dceReversal,
        block: this.userInfo.blockQuestion,
        version: "V17"
      };

      this.dceAnswers.push(answerObj);

      console.log(this.dceAnswers);

      this.selectedAnswer = "";
      this.name = this.itemOrder[this.itemOrder.indexOf(this.name) + 1];
    },
    chooseAnswer(item) {
      this.selectedAnswer = item;
      console.log(this.selectedAnswer);
    },
    getdceQuestion() {
      this.$axios
        .get("/api/question/dce", {
          params: { block: this.userInfo.blockQuestion }
        })
        .then(res => {
          //   this.dceQuestion = res.data;
          // console.log(res.data);
          // console.log(this.randomNum(1,2))
          var arrKey = [];
          var arrTemp = [];
          for (let i = 0; i < res.data.length; i++) {
            if (arrKey.indexOf(res.data[i].name) == -1) {
              arrKey.push(res.data[i].name);
            }
          }
          for (let i = 0; i < arrKey.length; i++) {
            var obj = {};
            for (let j = 0; j < res.data.length; j++) {
              if (res.data[j].name == arrKey[i]) {
                obj.name = arrKey[i];
                obj.presentation = res.data[j].presentation;
                if (res.data[j].answer == "A") {
                  obj.answerA = "A";
                  obj.sourceTextA = res.data[j].source_text;
                }
                if (res.data[j].answer == "B") {
                  obj.answerB = "B";
                  obj.sourceTextB = res.data[j].source_text;
                }
              }
            }
            arrTemp.push(obj);
          }
          console.log(arrTemp);
          this.dceQuestion = arrTemp;
          this.itemOrder = arrKey;
          this.name = this.dceQuestion[0].name;
        })
        .catch(error => {
          console.log(error);
        });
    },
    randomNum(minNum, maxNum) {
      switch (arguments.length) {
        case 1:
          return parseInt(Math.random() * minNum + 1, 10);
          break;
        case 2:
          return parseInt(Math.random() * (maxNum - minNum + 1) + minNum, 10);
          break;
        default:
          return 0;
          break;
      }
    }
  }
};
</script>
