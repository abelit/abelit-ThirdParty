<template>
  <v-container v-show="dceQuestion.length > 1" style="width: 1200px"
    <v-row>
      <v-col>
        <v-alert dense type="info">{{ eqLangLabels[$vuetify.lang.current].question }}</v-alert>
      </v-col>
    </v-row>
    <v-row v-for="item in dceQuestion" :key="item.id">
      <v-col cols="6" v-if="item.name == name">
        <v-card
          style="height:200px"
          class="pa-3"
          v-model="selectedAnswer"
          :class="item.answerA==selectedAnswer?'primary':''"
          @click="chooseAnswer(item.answerA)"
        >
          <h3>{{ item.answerA }}</h3>
          <div class="message-box-2 mt-5" v-if="randNum == 1">
            <div v-for="msg in item.sourceTextA.split('*')" :key="msg.key">
              <li v-if="msg != ''">
                <span>{{msg}}</span>
              </li>
            </div>
          </div>
          <div class="message-box-2 mt-5" v-else>
            <div v-for="msg in item.sourceTextB.split('*')" :key="msg.key">
              <li v-if="msg != ''">
                <span>{{msg}}</span>
              </li>
            </div>
          </div>
        </v-card>
      </v-col>
      <v-col cols="6" v-if="item.name == name">
        <v-card
          style="height:200px"
          class="pa-3"
          v-model="selectedAnswer"
          :class="item.answerB==selectedAnswer?'primary':''"
          @click="chooseAnswer(item.answerB)"
        >
          <h3>{{ item.answerB }}</h3>
          <div class="message-box-2 mt-5" v-if="randNum == 1">
            <div v-for="msg in item.sourceTextB.split('*')" :key="msg.key">
              <li v-if="msg != ''">
                <span>{{msg}}</span>
              </li>
            </div>
          </div>
          <div class="message-box-2 mt-5" v-else>
            <div v-for="msg in item.sourceTextA.split('*')" :key="msg.key">
              <li v-if="msg != ''">
                <span>{{msg}}</span>
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
    <v-row>
      <v-dialog v-model="popupDialog" persistent max-width="600">
        <v-card class="pt-5 yellow lighten-4">
          <v-card-text
            class="display-1"
            style="text-indent:2em;"
          >{{ eqLangLabels[$vuetify.lang.current].popup_example }}</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="light-green darken-3"
              @click="popupDialog = false"
              large
            >{{ eqLangLabels[$vuetify.lang.current].btn_ok_exmple }}</v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-dialog>
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
    randNum: 1,
    popupDialog: true
  }),
  created() {
    this.getdceQuestion();
    this.randNum = this.randomNum(1, 2);
    // console.log(this.randNum);
  },
  mounted() {},
  computed: {
    ...mapState(["userInfo", "examType", "qVersion", "eqLangLabels"])
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
        version: this.qVersion
      };

      this.dceAnswers.push(answerObj);

      // console.log(this.dceAnswers);

      this.selectedAnswer = "";
      this.name = this.itemOrder[this.itemOrder.indexOf(this.name) + 1];
    },
    chooseAnswer(item) {
      this.selectedAnswer = item;
      // console.log(this.selectedAnswer);
    },
    getdceQuestion() {
      this.$axios
        .get("/api/question/dce", {
          params: { block: this.userInfo.blockQuestion, version: this.qVersion }
        })
        .then(res => {
          var arrData = res.data.sort(() => Math.random() - 0.5);

          var arrKey = [];
          var arrTemp = [];
          for (let i = 0; i < arrData.length; i++) {
            if (arrKey.indexOf(arrData[i].name) == -1) {
              arrKey.push(arrData[i].name);
            }
          }
          for (let i = 0; i < arrKey.length; i++) {
            var obj = {};
            for (let j = 0; j < arrData.length; j++) {
              if (arrData[j].name == arrKey[i]) {
                obj.name = arrKey[i];
                obj.presentation = arrData[j].presentation;
                if (arrData[j].answer == "A") {
                  obj.answerA = "A";
                  obj.sourceTextA = arrData[j].source_text;
                }
                if (arrData[j].answer == "B") {
                  obj.answerB = "B";
                  obj.sourceTextB = arrData[j].source_text;
                }
              }
            }
            arrTemp.push(obj);
          }
          // console.log(arrTemp);
          this.dceQuestion = arrTemp;
          this.itemOrder = arrKey;
          this.name = this.dceQuestion[0].name;
          // console.log(this.dceQuestion);
          // let marr = [1,2,3,4,5,6,7,8,9]
          // marr.sort(() => Math.random() - 0.5);
          // console.log(marr)
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
