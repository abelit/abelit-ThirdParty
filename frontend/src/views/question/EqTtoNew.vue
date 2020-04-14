<template>
  <div class="grey lighten-5" style="width:1440px; margin:auto">
    <v-card justify="center" align="start">
      <v-card-title v-show="true">
        <v-row>
          <v-col>
            <v-alert dense type="info">{{
              eqLangLabels[$vuetify.lang.current].question
            }}</v-alert>
          </v-col>
        </v-row>
      </v-card-title>
      <v-card-text>
        <v-row style="height: 500px !important;">
          <v-col cols="3" class="px-8">
            <v-row justify="end">
              <v-col>
                <v-row justify="center" class="pt-8">
                  <v-btn class="black" @click="chooseAnswer('A')" fab dark
                    >A</v-btn
                  >
                </v-row>
                <div style="height:80px"></div>
                <v-row justify="center" class="my-6">
                  <v-btn class="red darken-3" @click="reset" large dark
                    ><v-icon>refresh</v-icon></v-btn
                  >
                </v-row>
                <div style="height:80px"></div>
                <v-row justify="center" class="my-2" style="margin-top:10px">
                  <v-btn class="black" @click="chooseAnswer('B')" fab dark
                    >B</v-btn
                  >
                </v-row>
                <v-row justify="center" class="my-2">
                  <v-btn
                    class="black"
                    dark
                    v-if="selectList.length > 0"
                    @click="reset"
                    disabled
                  >
                    <v-icon>refresh</v-icon>
                  </v-btn>
                </v-row>
              </v-col>
            </v-row>
          </v-col>
          <v-col cols="9" class="px-8" v-if="slide == 1">
            <v-row justify="start" align="center">
              <div style="position: relative;">
                <div
                  style="position: absolute;right:0px; z-index:99; top:-30px;"
                >
                  <div
                    style="background:#92d050;padding:10px 10px;width:200px;border-radius: 15px"
                  >
                    完全健康
                  </div>
                </div>
                <v-icon
                  style="color:#92d050;font-size:5rem; position: absolute;right:120px; z-index:98; top:-25px;"
                  >mdi-menu-down</v-icon
                >
                <div :style="cStyle1" style="text-align: center">
                  {{
                    Math.floor(currentYear) +
                      eqLangLabels[$vuetify.lang.current].years +
                      ((currentYear % 1) * 12 != 0
                        ? "," +
                          (currentYear % 1) * 12 +
                          eqLangLabels[$vuetify.lang.current].months
                        : "")
                  }}
                </div>
                <canvas id="canvas1" ref="canvas1"></canvas>
              </div>
              <table border="1" cellspacing="0" cellpadding="0" ref="table1">
                <tr style="height: 50px">
                  <td
                    v-for="item in allContent(topYear)"
                    :key="item"
                    style="text-align: center; width: 24px"
                    :class="
                      item <= 4 * currentYear
                        ? parseInt((item - 1) / 4) % 2 == 1
                          ? 'green lighten-1'
                          : 'green darken-3'
                        : ''
                    "
                  ></td>
                </tr>
              </table>
            </v-row>
            <div style="height:160px;"></div>
            <v-row justify="start" align="center" class="pt-12 mt-12">
              <table border="1" cellspacing="0" cellpadding="0" ref="table2">
                <tr style="height: 50px">
                  <td
                    v-for="item in allContent(topYear)"
                    :key="item"
                    style="text-align: center; width: 24px"
                    :class="
                      parseInt((item - 1) / 4) % 2 == 1
                        ? 'blue'
                        : 'blue darken-3'
                    "
                  ></td>
                </tr>
              </table>

              <div>
                <canvas id="canvas2" ref="canvas2"></canvas>
              </div>
              <div ref="tenyear" style="text-align: center;">10年</div>
            </v-row>
          </v-col>
          <v-col cols="9" class="px-8" v-if="slide == 2">
            <v-row justify="start">
              <div style="position: relative">
                <div
                  style="position: absolute;right:0px; z-index:99; top:-30px;"
                >
                  <div
                    style="background:#92d050;padding:10px 10px;width:200px;border-radius: 15px"
                  >
                    完全健康
                  </div>
                </div>
                <v-icon
                  style="color:#92d050;font-size:5rem; position: absolute;right:120px; z-index:98; top:-25px;"
                  >mdi-menu-down</v-icon
                >
                <div :style="cStyle3" style="text-align: center">
                  {{
                    Math.floor(currentYearB) +
                      eqLangLabels[$vuetify.lang.current].years +
                      ((currentYearB % 1) * 12 != 0
                        ? "," +
                          (currentYearB % 1) * 12 +
                          eqLangLabels[$vuetify.lang.current].months
                        : "")
                  }}
                </div>
                <canvas id="canvas3" ref="canvas3"></canvas>
              </div>
              <!-- <table border="1" cellspacing="0" cellpadding="0" ref="table3">
                <tr style="height: 50px">
                  <td
                    v-for="item in allContent(topYearB)"
                    :key="item"
                    style="text-align: center; width: 16px"
                    :class="
                      item <= 4 * currentYearB ? (parseInt((item - 1) / 4) % 2 == 1?'green lighten-1':'green darken-3') : ''
                    "
                  ></td>
                </tr>
              </table>-->
              <table border="1" cellspacing="0" cellpadding="0" ref="table3">
                <tr style="height: 50px">
                  <td
                    v-for="item in allContent(topYearB)"
                    :key="item"
                    style="text-align: center; width: 16px"
                    :class="
                      item <= 4 * currentYearB
                        ? parseInt((item - 1) / 4) % 2 == 1
                          ? 'green lighten-1'
                          : 'green darken-3'
                        : ''
                    "
                  ></td>
                </tr>
              </table>
            </v-row>
            <div style="height:160px;"></div>
            <v-row justify="start" align="center" class="pt-12 mt-12">
              <table border="1" cellspacing="0" cellpadding="0" ref="table4">
                <tr style="height: 50px">
                  <td
                    v-for="item in allContent(topYearB)"
                    :key="item"
                    style="text-align: center; width: 16px"
                    :class="
                      item <= 40
                        ? parseInt((item - 1) / 4) % 2 == 1
                          ? 'green lighten-1'
                          : 'green darken-3'
                        : parseInt((item - 1) / 4) % 2 == 1
                        ? 'blue lighten-1'
                        : 'blue darken-3'
                    "
                  ></td>
                </tr>
              </table>

              <div>
                <canvas id="canvas4" ref="canvas4"></canvas>

                <canvas id="canvas5" ref="canvas5"></canvas>
              </div>
              <div style="width:100%" ref="tip_w">
                <div
                  ref="tenyear4"
                  style="width:50%;text-align: center;float:left"
                >
                  10年完全健康
                </div>
                <div
                  ref="tenyear5"
                  style="width:50%;text-align: center;float:right"
                >
                  10年
                </div>
              </div>
            </v-row>
          </v-col>
        </v-row>
        <v-row
          justify="center"
          align="center"
          v-if="slide == 1 && block.source_text"
        >
          <v-col cols="6">
            <v-row>
              <div style="position: relative;height:180px;">
                <v-icon
                  style="color:#5b9bd5;font-size:5rem; position: absolute;left:250px; z-index:98; top:-45px;"
                  >mdi-menu-up</v-icon
                >
                <div style>
                  <div
                    style="background:#5b9bd5;padding:10px 10px;width:400px;border-radius: 15px;height:180px"
                  >
                    <div
                      v-for="msg in block.source_text.split('*')"
                      :key="msg.key"
                    >
                      <li v-if="msg != ''">
                        <span>{{ msg }}</span>
                      </li>
                    </div>
                  </div>
                </div>
              </div>
            </v-row>
          </v-col>
        </v-row>
        <div v-if="slide == 2" ref="infotip" style="height:180px" class="mt-5">
          <div style="float:left;position: absolute;left:450px">
            <v-row style="position: relative;">
              <v-icon
                style="color:#92d050;font-size:5rem; position: absolute;left:250px; z-index:98; top:-45px;"
                >mdi-menu-up</v-icon
              >

              <div
                style="background:#92d050;padding:10px 10px;width:400px;border-radius: 15px;height:180px"
              >
                完全健康
              </div>
            </v-row>
          </div>
          <div style="float:right; position: absolute;right:100px">
            <v-row style="position: relative;">
              <v-icon
                style="color:#5b9bd5;font-size:5rem; position: absolute;left:250px; z-index:98; top:-45px;"
                >mdi-menu-up</v-icon
              >

              <div
                style="background:#5b9bd5;padding:10px 10px;width:400px;border-radius: 15px;height:180px"
              >
                <div v-for="msg in block.source_text.split('*')" :key="msg.key">
                  <li v-if="msg != ''">
                    <span>{{ msg }}</span>
                  </li>
                </div>
              </div>
            </v-row>
          </div>
        </div>
        <v-row justify="center" align="center"></v-row>
      </v-card-text>
      <v-divider></v-divider>
    </v-card>
    <!-- <v-row>
      <v-dialog v-model="popupDialog" persistent max-width="600">
        <v-card class="pt-5 yellow lighten-4">
          <v-card-text class="display-1">{{ popMsg }}</v-card-text>
          <v-card-actions v-if="!popAB">
            <v-spacer></v-spacer>
            <v-btn
              color="light-green darken-3"
              @click="closeDialog"
              large
            >{{ eqLangLabels[$vuetify.lang.current].btn_ok_exmple }}</v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
          <v-card-actions v-else>
            <v-spacer></v-spacer>
            <v-btn color="light-green darken-3" @click="submitAnswer('Y')" large>是</v-btn>
            <v-btn color="light-green darken-3" @click="submitAnswer('N')" large>否</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>-->

    <v-row class="page-1">
      <v-dialog v-model="openQDialog" persistent max-width="480">
        <v-card outlined>
          <v-card-title class="blue darken-1 font-weight-wwhite"
            >开放式问题：请填写您偏好的年份？</v-card-title
          >
          <v-divider></v-divider>
          <v-card-text style="overflow: hidden;" class="px-0 py-0 mt-3">
            <v-form ref="form" v-model="valid" lazy-validation>
              <v-row align="center" justify="center">
                <v-col cols="12" sm="6" md="8">
                  <v-text-field
                    v-model="opYear"
                    label="填写年份"
                    outlined
                    :rules="[rules.required, rules.numRequired]"
                    dense
                    required
                  ></v-text-field>
                </v-col>
              </v-row>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-3" @click="submitAnswer()" dark large
              >是</v-btn
            >

            <v-btn class="red darken-3" @click="reset" large dark
              ><v-icon>refresh</v-icon></v-btn
            >
            <v-spacer></v-spacer>
            <!-- <v-btn color="black darken-3" @click="submitAnswer('N')" dark>否</v-btn> -->
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
    <v-row>
      <v-dialog v-model="popupDialog2" persistent max-width="600">
        <v-card class="pt-5 yellow lighten-4">
          <v-card-text class="display-1">{{ popMsg }}</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="light-green darken-3"
              @click="submitAnswer2('Y')"
              large
              >是</v-btn
            >
            <v-btn
              color="light-green darken-3"
              @click="submitAnswer2('N')"
              large
              >否</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "EqTto",
  props: ["block", "startTime"],
  data: () => ({
    cStyle1: "",
    cStyle3: "",
    showDetail: true,
    currentYear: 5,
    topYear: 10,
    step: 0,
    currentYearB: 10,
    topYearB: 20,
    stepB: 0,
    selected: [],
    tableWidth: "",
    slide: 1,
    stepDirection: 0,
    resets: 0,
    bAlertText: "",
    newttoAnswer: "",
    popupDialog: false,
    popupDialog2: false,
    popAB: false,
    popMsg: "",
    randomYear: Math.floor(Math.random() * 6) + 2,
    randomYearB: "",
    selectList: [],
    openQDialog: false,
    ticksLabels: Array.from({ length: 21 }, (v, k) => k / 2),
    yearRange: [0, 10],
    rules: {
      required: value => !!value || "年份为必填项.",
      numRequired: v =>
        !!((v * 10) % 5 == 0 && v >= 0 && v <= 10) ||
        "填写的年份应在0-10之间，且只包含半年或整年，如1.5，1"
    },
    opYearType: "",
    opYear: "",
    opYearStart: "",
    opYearEnd: "",
    radio1: "",
    radio2: "",
    valid: true
  }),
  watch: {
    opYear(val) {
      if (val >= 0 && val <= 10 && (val * 10) % 5 === 0) {
        if (this.slide == 1) {
          this.currentYear = val;
          this.$nextTick(() => {
            this.drawLine(
              "canvas1",
              this.$refs.table1.offsetWidth,
              20,
              (this.$refs.table1.offsetWidth / this.topYear) * this.currentYear,
              10,
              0
            );
            this.cStyle1 = this.getStyle(
              this.$refs.table1.offsetWidth,
              this.topYear,
              this.currentYear == 0
                ? 0.5
                : this.currentYear == 0.5
                ? 0.8
                : this.currentYear
            );
          });
        } else {
          this.currentYearB = val;
          this.$nextTick(() => {
            this.drawLine(
              "canvas3",
              this.$refs.table3.offsetWidth,
              20,
              ((this.$refs.table3.offsetWidth / this.topYear) *
                this.currentYearB) /
                2,
              10,
              0
            );
            this.cStyle3 = this.getStyle(
              this.$refs.table3.offsetWidth,
              this.topYearB,
              this.currentYearB == 0
                ? 1
                : this.currentYearB == 0.5
                ? 1.5
                : this.currentYearB
            );
          });
        }
      }
    },
    opYearEnd(value) {
      // if (val < this.opYearStart && this.opYearStart != " ") {
      //   // this.opYearEnd = ""
      //   alert("结束年份不能小于起始年份")
      //   return
      // }

      let val = parseFloat(value);

      if (
        val >= 0 &&
        val <= 10 &&
        (val * 10) % 5 == 0 &&
        this.opYearStart >= 0 &&
        this.opYearStart <= 10 &&
        this.opYearStart <= val &&
        (this.opYearStart * 10) % 5 == 0
      ) {
        if (this.slide == 1) {
          this.currentYear = val;
          this.$nextTick(() => {
            this.drawLine(
              "canvas1",
              this.$refs.table1.offsetWidth,
              20,
              (this.$refs.table1.offsetWidth / this.topYear) * this.opYearEnd -
                (this.$refs.table1.offsetWidth / this.topYear) *
                  this.opYearStart,
              10,
              (this.$refs.table1.offsetWidth / this.topYear) * this.opYearStart
            );
            this.cStyle1 = this.getStyle(
              this.$refs.table1.offsetWidth,
              this.topYear,
              this.currentYear == 0
                ? 0.5
                : this.currentYear == 0.5
                ? 0.8
                : this.currentYear
            );
          });
        } else {
          this.currentYearB = val;
          this.$nextTick(() => {
            this.drawLine(
              "canvas3",
              this.$refs.table3.offsetWidth,
              20,
              ((this.$refs.table3.offsetWidth / this.topYear) *
                this.currentYearB) /
                2 -
                ((this.$refs.table3.offsetWidth / this.topYear) *
                  this.opYearStart) /
                  2,
              10,
              ((this.$refs.table3.offsetWidth / this.topYear) *
                this.opYearStart) /
                2
            );
            this.cStyle3 = this.getStyle(
              this.$refs.table3.offsetWidth,
              this.topYearB,
              this.currentYearB == 0
                ? 1
                : this.currentYearB == 0.5
                ? 1.5
                : this.currentYearB
            );
          });
        }
      }
    },
    opYearStart(value) {
      // if (val > this.opYearEnd && this.opYearEnd != " ") {
      //   // this.opYearStart = ""
      //   alert("起始年份不能大于结束年份")
      //   return;
      // }
      let val = parseFloat(value);
      if (
        val >= 0 &&
        val <= 10 &&
        (val * 10) % 5 === 0 &&
        val <= this.opYearEnd &&
        this.opYearEnd <= 10 &&
        this.opYearEnd >= 0 &&
        (this.opYearEnd * 10) % 5 === 0
      ) {
        if (this.slide == 1) {
          this.opYearStart = val;
          this.$nextTick(() => {
            this.drawLine(
              "canvas1",
              this.$refs.table1.offsetWidth,
              20,
              (this.$refs.table1.offsetWidth / this.topYear) * this.opYearEnd -
                (this.$refs.table1.offsetWidth / this.topYear) *
                  this.opYearStart,
              10,
              (this.$refs.table1.offsetWidth / this.topYear) * this.opYearStart
            );
            this.cStyle1 = this.getStyle(
              this.$refs.table1.offsetWidth,
              this.topYear,
              this.currentYear == 0
                ? 0.5
                : this.currentYear == 0.5
                ? 0.8
                : this.currentYear
            );
          });
        } else {
          // this.currentYearB = val;
          this.$nextTick(() => {
            this.drawLine(
              "canvas3",
              this.$refs.table3.offsetWidth,
              20,
              ((this.$refs.table3.offsetWidth / this.topYear) *
                this.currentYearB) /
                2 -
                ((this.$refs.table3.offsetWidth / this.topYear) *
                  this.opYearStart) /
                  2,
              10,
              ((this.$refs.table3.offsetWidth / this.topYear) *
                this.opYearStart) /
                2
            );
            this.cStyle3 = this.getStyle(
              this.$refs.table3.offsetWidth,
              this.topYearB,
              this.currentYearB == 0
                ? 1
                : this.currentYearB == 0.5
                ? 1.5
                : this.currentYearB
            );
          });
        }
      }
    }
  },

  methods: {
    test() {
      console.log(this.yearRange);
      this.openQDialog = false;
    },
    submitAnswer() {
      if (this.opYear == '' || this.opYear * 10 % 5 != 0 || this.opYear >10 ||this.opYear < 0) {
        alert("请填写符合条件的答案，通常，填写的年份在0~10之间，且小数部分只能包含0.5（如5, 5.5）。");
        return;
      }
      this.popupDialog2 = true;
      this.genPoppupMsg(this.slide);
    },
    submitAnswer2(value) {
      // 验证是否选择开放式问题
      // this.$refs.form.validate();
      if (value == "N") {
        this.popupDialog2 = false;
        return;
      }
      if (
        !(
          (this.opYearType == 1 &&
            this.opYear >= 0 &&
            this.opYear <= 10 &&
            (this.opYear * 10) % 5 == 0) ||
          (this.opYearType == 2 &&
            this.opYearStart >= 0 &&
            this.opYearStart <= 10 &&
            this.opYearEnd >= 0 &&
            this.opYearEnd <= 10 &&
            this.opYearStart <= this.opYearEnd &&
            (this.opYearStart * 10) % 5 == 0 &&
            (this.opYearEnd * 10) % 5 == 0)
        )
      ) {
        alert(
          "请填写符合条件的答案，通常，填写的年份在0~10之间，且小数部分只能包含0.5（如5, 5.5），若为时间范围，开始值应该小于结束值。"
        );
        return;
      }

      var answerObj = {
        questionid: this.examType.id,
        participant: this.userInfo.participant,
        interviewer: this.userInfo.interviewer,
        item: this.block.name,
        position_of_item: this.block.id,
        block: this.block.block,
        start_year_random: this.randomYear,
        select1: "",
        select2: "",
        select3: "",
        select4: "",
        open_select: "",
        end_year_random: this.randomYearB,
        version: this.qVersion,
        reset: this.resets
      };

      let [s1, s2, s3, s4] = this.selectList;

      answerObj.select1 = s1 || "";
      answerObj.select2 = s2 || "";
      answerObj.select3 = s3 || "";
      answerObj.select4 = s4 || "";

      if (this.opYearType == 1) {
        answerObj.open_select = this.opYear;
      } else {
        answerObj.open_select = this.opYearStart + "~" + this.opYearEnd;
      }

      this.newttoAnswer = answerObj;

      // console.log(this.newttoAnswer);

      // //通过改变父组件的值
      this.openQDialog = false;
      this.updateItem();
    },
    genPoppupMsg(type) {
      //   opYearType: "",
      // opYear: "",
      // opYearStart: "",
      // opYearEnd: "",
      if (type == 1) {
        let displayYear1 =
          this.opYearType == 1
            ? 10 - this.opYear
            : (10 - this.opYearEnd).toString() +
              "~" +
              (10 - this.opYearStart).toString();

        this.popMsg =
          this.eqLangLabels[this.$vuetify.lang.current].msg_response_41 +
          displayYear1 +
          this.eqLangLabels[this.$vuetify.lang.current].msg_response_42;
      }
      if (type == 2) {
        let displayYear2 =
          this.opYearType == 1
            ? 20 - this.opYear
            : (20 - this.opYearEnd).toString() +
              "~" +
              (20 - this.opYearStart).toString();

        this.popMsg =
          this.eqLangLabels[this.$vuetify.lang.current].msg_response_51 +
          displayYear2 +
          this.eqLangLabels[this.$vuetify.lang.current].msg_response_52;
      }
    },
    reset() {
      this.resets++;
      this.slide = 1;
      this.cStyle1 = "";
      this.cStyle3 = "";
      this.showDetail = true;
      // this.currentYear = 5;
      this.topYear = 10;
      this.step = 0;
      this.currentYearB = 10;
      this.topYearB = 20;
      this.stepB = 0;
      this.selected = [];
      this.tableWidth = "";
      this.slide = 1;
      this.stepDirection = 0;
      this.bAlertText = "";
      this.newttoAnswer = "";
      this.popupDialog = false;
      this.popupDialog2 = false;
      this.popAB = false;
      this.popMsg = "";
      this.randomYear = Math.floor(Math.random() * 6) + 2;
      this.randomYearB = "";
      this.selectList = [];
      this.openQDialog = false;
      this.opYearType = "";
      this.opYear = "";
      this.opYearStart = "";
      this.opYearEnd = "";
      this.radio1 = "";
      this.radio2 = "";
      this.valid = true;


      this.currentYear = this.randomYear;

      this.$nextTick(() => {
        if (this.slide === 1) {
          this.drawLine(
            "canvas1",
            this.$refs.table1.offsetWidth,
            20,
            (this.$refs.table1.offsetWidth / this.topYear) * this.currentYear,
            10,
            0
          );
          this.cStyle1 = this.getStyle(
            this.$refs.table1.offsetWidth,
            this.topYear,
            this.currentYear == 0
              ? 0.5
              : this.currentYear == 0.5
              ? 0.8
              : this.currentYear
          );
          this.drawLine(
            "canvas2",
            this.$refs.table2.offsetWidth,
            20,
            this.$refs.table2.offsetWidth,
            10,
            0
          );
        }
        if (this.slide === 2) {
          this.drawLine(
            "canvas3",
            this.$refs.table3.offsetWidth,
            20,
            (this.$refs.table3.offsetWidth / this.topYearB) * this.currentYearB,
            10,
            0
          );
          this.cStyle3 = this.getStyle(
            this.$refs.table3.offsetWidth,
            this.topYearB,
            this.currentYearB == 0
              ? 1
              : this.currentYearB == 0.5
              ? 1.5
              : this.currentYearB
          );
        }
      });
    },
    chooseAnswer(type) {
      this.opYearType = 1;
      switch (this.selectList.length) {
        case 0:
          this.currentYear = type == "A" ? 1 : 9;
          break;
        case 1:
          if (this.selectList[0] === "B") {
            this.openQDialog = true;
          } else {
            this.currentYear = type == "A" ? 0 : 1;
            this.openQDialog = type == "B";
          }
          break;
        case 2:
          this.slide = type == "A" ? 2 : 1;
          this.randomYearB = Math.floor(Math.random() * 6) + 2;
          this.currentYearB = this.randomYearB;
          this.openQDialog = type == "B";
          if (this.slide == 2) {
            this.opYear = "";
            this.opYearType = "";
            this.opYearStart = "";
            this.opYearEnd = "";
          }
          break;
        case 3:
          this.openQDialog = true;
          break;
        default:
          return;
      }
      this.selectList.push(type);
      console.log(this.selectList);
      console.log(this.currentYear);
      console.log(this.currentYearB);

      // if (type === "A") {
      //   this.currentYear = 1;
      // }
      // 生成样式
      this.$nextTick(() => {
        if (this.slide === 1) {
          this.drawLine(
            "canvas1",
            this.$refs.table1.offsetWidth,
            20,
            (this.$refs.table1.offsetWidth / this.topYear) * this.currentYear,
            10,
            0
          );
          this.cStyle1 = this.getStyle(
            this.$refs.table1.offsetWidth,
            this.topYear,
            this.currentYear == 0
              ? 0.5
              : this.currentYear == 0.5
              ? 0.8
              : this.currentYear
          );
          this.drawLine(
            "canvas2",
            this.$refs.table2.offsetWidth,
            20,
            this.$refs.table2.offsetWidth,
            10,
            0
          );
        }
        if (this.slide === 2) {
          this.drawLine(
            "canvas3",
            this.$refs.table3.offsetWidth,
            20,
            (this.$refs.table3.offsetWidth / this.topYearB) * this.currentYearB,
            10,
            0
          );
          this.cStyle3 = this.getStyle(
            this.$refs.table3.offsetWidth,
            this.topYearB,
            this.currentYearB == 0
              ? 1
              : this.currentYearB == 0.5
              ? 1.5
              : this.currentYearB
          );
        }
      });
    },

    drawLine(c, w, h, l, top, left) {
      //获取画板
      var canvas = document.getElementById(c);

      if (canvas == null) return false;

      canvas.height = h;
      canvas.width = w;

      if (l === 0) return false;

      //获取画笔
      var ctx = canvas.getContext("2d");
      //画线
      //横  （向右）
      drawArrowLine(ctx, 0, top, 0 + left + 5, 0, l + left - 5, 0);
      //横  （向左）
      drawArrowLine(ctx, 0 + left + 5, 0, 5, 0, 0, 0);
      //画带箭头的线
      function drawArrowLine(ctx, ox, oy, x1, y1, x2, y2) {
        //参数说明 canvas的 id ，原点坐标  第一个端点的坐标，第二个端点的坐标
        var sta = new Array(x1, y1);
        var end = new Array(x2, y2);
        //画线
        ctx.beginPath();
        //坐标源点
        ctx.translate(ox, oy, 0);
        ctx.moveTo(sta[0], sta[1]);
        ctx.lineTo(end[0], end[1]);
        ctx.fill();
        ctx.stroke();
        ctx.save();
        //画箭头
        ctx.translate(end[0], end[1]);
        //我的箭头本垂直向下，算出直线偏离Y的角，然后旋转 ,rotate是顺时针旋转的，所以加个负号
        var ang = (end[0] - sta[0]) / (end[1] - sta[1]);
        ang = Math.atan(ang);
        if (end[1] - sta[1] >= 0) {
          ctx.rotate(-ang);
        } else {
          // 旋转180度
          ctx.rotate(Math.PI - ang);
        }
        ctx.lineTo(-5, -10);
        ctx.lineTo(0, -5);
        ctx.lineTo(5, -10);
        ctx.lineTo(0, 0);
        ctx.fill();
        // ctx.fillText("hello abelit",50,90);
        // ctx.textAlign = center;
        ctx.restore();
        ctx.closePath();
      }
    },
    getStyle(w, ty, cy) {
      var width = w;
      var paddingRight = w - (w / ty) * cy;
      if (width == paddingRight) {
        paddingRight = paddingRight - 30;
      }
      return (
        "width: " + width + "px; " + "padding-right: " + paddingRight + "px;"
      );
    },
    updateItem() {
      this.$emit("cUpdateItem", this.newttoAnswer);
    },
    closeDialog() {
      this.popupDialog = false;
      this.popA = false;
      this.popB = false;
      this.popA_to_B = false;
      this.popAZero = false;
      this.popBFull = false;
    }
  },
  mounted() {
    // let rangeArray = (start, end) =>
    //   Array(end - start + 1)
    //     .fill(0)
    //     .map((v, i) => i / 2 + start);

    // console.log(rangeArray(0, 20));

    // console.log(Array.from({ length: 21 }, (v, k) => k / 2));
    // console.log(1.5 % 0.5);
    // let arr1 = ["A", "B"];
    // let obj = {
    //   block: 1,
    //   item: 1,
    //   select1: "",
    //   select2: "",
    //   select3: "",
    //   select4: ""
    // };
    // let [select1, select2, select3, select4] = arr1;

    // obj.select1 = select1;
    // obj.select2 = select2;
    // obj.select3 = select3;
    // obj.select4 = select4;

    // console.log(obj);

    // 随机生成2~8年

    this.currentYear = this.randomYear;
    // 生成样式
    this.cStyle1 = this.getStyle(
      this.$refs.table1.offsetWidth,
      this.topYear,
      this.currentYear == 0
        ? 0.5
        : this.currentYear == 0.5
        ? 0.8
        : this.currentYear
    );
    this.drawLine(
      "canvas1",
      this.$refs.table1.offsetWidth,
      20,
      (this.$refs.table1.offsetWidth / this.topYear) * this.currentYear,
      10,
      0
    );
    this.drawLine(
      "canvas2",
      this.$refs.table2.offsetWidth,
      20,
      this.$refs.table2.offsetWidth,
      10,
      0
    );
    this.$refs.tenyear.style.width = this.$refs.table2.offsetWidth + "px";
  },
  computed: {
    allContent: function() {
      return function(year) {
        var arr = [];
        for (var i = 1; i <= 4 * year; i++) {
          arr.push(i);
        }
        return arr;
      };
    },
    ...mapState(["userInfo", "examType", "qVersion", "eqLangLabels"])
  }
};
</script>

<style lang="scss" scoped>
.v-dialog__content {
  padding-bottom: 20px;
}
.v-dialog__content {
  margin-top: -25px;
}
.message-box {
  position: relative;
  width: 400px;
  height: 200px;
  left: 0px;
  border: 2px solid #74a1e0;
  background-color: #74a1e0;
  border-radius: 25px;
}
.message-box:before {
  position: absolute;
  content: "";
  width: 0;
  height: 0;
  left: 200px;
  top: -90px;

  border-top: 60px solid transparent;
  border-right: 10px solid transparent;
  border-bottom: 30px solid #74a1e0;
  border-left: 120px solid transparent;
}
.message-box-1 {
  position: relative;
  width: 400px;
  height: 200px;
  left: 0px;

  border: 2px solid #9ccc65;
  background-color: #9ccc65;
  border-radius: 25px;
}
.message-box-1:before {
  position: absolute;
  content: "";
  width: 0;
  height: 0;
  left: 200px;
  top: -90px;

  border-top: 60px solid transparent;
  border-right: 120px solid transparent;
  border-bottom: 30px solid #9ccc65;
  border-left: 10px solid transparent;
}
.message-box-2 {
  position: relative;
  float: left;
  top: -240px;
  width: 400px;
  height: 200px;
  left: 600px;
  border: 2px solid #74a1e0;
  background-color: #74a1e0;
  border-radius: 25px;
}
.message-box-2:before {
  position: absolute;
  content: "";
  width: 0;
  height: 0;
  left: 200px;
  top: -90px;

  border-top: 60px solid transparent;
  border-right: 10px solid transparent;
  border-bottom: 30px solid #74a1e0;
  border-left: 120px solid transparent;
}
* {
  font-size: 1.2rem;
}
</style>
