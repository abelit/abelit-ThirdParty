<template>
  <div class="grey lighten-5" style="width: 1440px; margin: auto">
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
        <v-row style="height: 800px !important">
          <v-col cols="3" class="px-8">
            <v-row justify="end">
              <v-col>
                <v-row justify="center" class="pt-8">
                  <v-btn class="black" @click="chooseAnswer('A')" fab dark
                    >A</v-btn
                  >
                </v-row>
                <v-row justify="center" class="my-6">
                  <v-btn
                    class="black darken-3"
                    @click="chooseAnswer('AB')"
                    large
                    dark
                    >A & B</v-btn
                  >
                </v-row>
                <v-row justify="center" class="my-2" style="margin-top: 10px">
                  <v-btn class="black" @click="chooseAnswer('B')" fab dark
                    >B</v-btn
                  >
                </v-row>
                <v-row justify="center" class="my-2">
                  <v-btn class="black" dark v-if="step > 0" @click="reset">
                    <v-icon>refresh</v-icon>
                  </v-btn>
                </v-row>
              </v-col>
            </v-row>
          </v-col>
          <v-col cols="9" class="px-8" v-if="slide == 1">
               <v-row justify="start" align="center" >
              <div style="position: relative">
                <div
                  style="
                    position: absolute;
                    right: 0px;
                    z-index: 99;
                    top: -30px;
                  "
                >
                  <div
                    style="
                      background: #92d050;
                      padding: 10px 10px;
                      width: 200px;
                      border-radius: 15px;
                    "
                  >
                    完全健康
                  </div>
                </div>
                <v-icon
                  style="
                    color: #92d050;
                    font-size: 5rem;
                    position: absolute;
                    right: 120px;
                    z-index: 98;
                    top: -25px;
                  "
                  >mdi-menu-down</v-icon
                >
                <div :style="cStyle11" style="text-align: center">
                  您的孩子： 10年
                </div>
                <canvas id="canvas11" ref="canvas11"></canvas>
              </div>
              <table border="1" cellspacing="0" cellpadding="0" ref="table11">
                <tr style="height: 50px">
                  <td
                    v-for="item in allContent(topYear)"
                    :key="item"
                    style="text-align: center; width: 24px"
                    :class="
                    parseInt((item - 1) / 4) % 2 == 1
                          ? 'green lighten-1'
                          : 'green darken-3'
                 
                    "
                  ></td>
                </tr>
              </table>
            </v-row>

            <v-row justify="start" align="center" style="margin-top: 40px">
              <div style="position: relative">
                <div
                  style="
                    position: absolute;
                    right: 0px;
                    z-index: 99;
                    top: -30px;
                  "
                >
                  <div
                    style="
                      background: #92d050;
                      padding: 10px 10px;
                      width: 200px;
                      border-radius: 15px;
                    "
                  >
                    完全健康
                  </div>
                </div>
                <v-icon
                  style="
                    color: #92d050;
                    font-size: 5rem;
                    position: absolute;
                    right: 120px;
                    z-index: 98;
                    top: -25px;
                  "
                  >mdi-menu-down</v-icon
                >
                <div :style="cStyle11" style="text-align: center" ref="fixdiv">
                  您自己： {{
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

         
            <v-row justify="start" align="center" class="mt-10">
              <div style="position: relative">
         
                <v-icon
                  style="
                    color: #5b9bd5;
                    font-size: 5rem;
                    position: absolute;
                    left: 20px;
                    z-index: 98;
                    top: 85px;
                  "
                  >mdi-menu-down</v-icon
                >
                <div style>
                  <div
                    style="
                      background: #5b9bd5;
                      padding: 10px 10px;
                      width: 300px;
                      border-radius: 15px;
                      height: 120px;
                    "
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
                <div ref="tenyear" style="text-align: center">您的孩子： 10年</div>
                <canvas id="canvas2" ref="canvas2"></canvas>
              </div>
              
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
            </v-row>

            <v-row justify="start" align="center" class="pt-12 mt-12">
              <div style="position: relative">
                <div
                  style="position: absolute; left: 0px; z-index: 99; top: -30px"
                >
                  <div
                    style="
                      background: #92d050;
                      padding: 10px 10px;
                      width: 200px;
                      border-radius: 15px;
                    "
                  >
                    完全健康
                  </div>
                </div>
                <v-icon
                  style="
                    color: #92d050;
                    font-size: 5rem;
                    position: absolute;
                    left: 120px;
                    z-index: 98;
                    top: -25px;
                  "
                  >mdi-menu-down</v-icon
                >
                <div ref="tenyear" style="text-align: center">您自己： 10年</div>
                <canvas id="canvas12" ref="canvas12"></canvas>
              </div>
              
              <table border="1" cellspacing="0" cellpadding="0" ref="table12">
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
            </v-row>
          </v-col>
          <v-col cols="9" class="px-8" v-if="slide == 2">
            <v-row justify="start">
              <div style="position: relative">
                <div
                  style="
                    position: absolute;
                    right: 0px;
                    z-index: 99;
                    top: -30px;
                  "
                >
                  <div
                    style="
                      background: #92d050;
                      padding: 10px 10px;
                      width: 200px;
                      border-radius: 15px;
                    "
                  >
                    完全健康
                  </div>
                </div>
                <v-icon
                  style="
                    color: #92d050;
                    font-size: 5rem;
                    position: absolute;
                    right: 120px;
                    z-index: 98;
                    top: -25px;
                  "
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
              <div style="width: 100%" ref="tip_w">
                <div
                  ref="tenyear4"
                  style="width: 50%; text-align: center; float: left"
                >
                  10年完全健康
                </div>
                <div
                  ref="tenyear5"
                  style="width: 50%; text-align: center; float: right"
                >
                  10年
                </div>
              </div>
            </v-row>
          </v-col>
        </v-row>
        <!-- <v-row
          justify="center"
          align="center"
          v-if="slide == 1 && block.source_text"
        >
          <v-col cols="6">
            <v-row>
              <div style="position: relative; height: 180px">
                <v-icon
                  style="
                    color: #5b9bd5;
                    font-size: 5rem;
                    position: absolute;
                    left: 250px;
                    z-index: 98;
                    top: -45px;
                  "
                  >mdi-menu-up</v-icon
                >
                <div style>
                  <div
                    style="
                      background: #5b9bd5;
                      padding: 10px 10px;
                      width: 400px;
                      border-radius: 15px;
                      height: 180px;
                    "
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
        </v-row> -->
        <div v-if="slide == 2" ref="infotip" style="height: 180px" class="mt-5">
          <div style="float: left; position: absolute; left: 450px">
            <v-row style="position: relative">
              <v-icon
                style="
                  color: #92d050;
                  font-size: 5rem;
                  position: absolute;
                  left: 250px;
                  z-index: 98;
                  top: -45px;
                "
                >mdi-menu-up</v-icon
              >

              <div
                style="
                  background: #92d050;
                  padding: 10px 10px;
                  width: 400px;
                  border-radius: 15px;
                  height: 180px;
                "
              >
                完全健康
              </div>
            </v-row>
          </div>
          <!-- <div style="float: right; position: absolute; right: 100px">
            <v-row style="position: relative">
              <v-icon
                style="
                  color: #5b9bd5;
                  font-size: 5rem;
                  position: absolute;
                  left: 250px;
                  z-index: 98;
                  top: -45px;
                "
                >mdi-menu-up</v-icon
              >

              <div
                style="
                  background: #5b9bd5;
                  padding: 10px 10px;
                  width: 400px;
                  border-radius: 15px;
                  height: 180px;
                "
              >
                <div v-for="msg in block.source_text.split('*')" :key="msg.key">
                  <li v-if="msg != ''">
                    <span>{{ msg }}</span>
                  </li>
                </div>
              </div>
            </v-row>
          </div> -->
        </div>
        <v-row justify="center" align="center"></v-row>
      </v-card-text>
      <v-divider></v-divider>
    </v-card>
    <v-row>
      <v-dialog v-model="popupDialog" persistent max-width="600">
        <v-card class="pt-5 yellow lighten-4">
          <v-card-text class="display-1">{{ popMsg }}</v-card-text>
          <v-card-actions v-if="!popAB">
            <v-spacer></v-spacer>
            <v-btn color="light-green darken-3" @click="closeDialog" large>{{
              eqLangLabels[$vuetify.lang.current].btn_ok_exmple
            }}</v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
          <v-card-actions v-else>
            <v-spacer></v-spacer>
            <v-btn color="light-green darken-3" @click="submitAnswer('Y')" large
              >是</v-btn
            >
            <v-btn color="light-green darken-3" @click="submitAnswer('N')" large
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
    currentYear: 10,
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
    currentTime: "",
    // startTime: 0,
    endTime: 0,
    usedTime: "00:00:00",
    itemStartTime: 0,
    itemEndTime: 0,
    itemUsedTime: "00:00:00",
    bAlertText: "",
    ttoAnswer: "",
    popupDialog: false,
    // popA: false,
    // popB: false,
    // popA_to_B: false,
    // popAZero: false,
    // popBFull: false,
    popAB: false,
    popMsg: "",
    // newBlock: ""
  }),

  methods: {
    submitAnswer(value) {
      if (value == "Y") {
        var ttoValue = 0;
        if (this.stepDirection % 2 == 0) {
          ttoValue = this.currentYear * 0.1;
        } else {
          ttoValue = (this.currentYearB - 10) * 0.1;
        }
        var answerObj = {
          questionid: this.examType.id,
          participant: this.userInfo.participant,
          interviewer: this.userInfo.interviewer,
          item: this.block.name,
          position_of_item: this.block.id,
          tto_value: ttoValue.toFixed(2),
          used_time: this.countTime(this.itemUsedTime),
          composite_switches: this.stepDirection,
          resets: this.resets,
          number_of_moves: this.step,
          block: this.block.block,
          version: this.qVersion,
        };
        this.ttoAnswer = answerObj;

        // console.log("本题用时：" + this.itemUsedTime);
        this.itemStartTime = new Date();
        this.itemEndTime = 0;
        this.itemUsedTime = "00:00:00";
        this.getUsedTime();
        // this.reset();
        // //通过改变父组件的值
        this.updateItem();
        this.popupDialog = false;
      } else {
        this.popupDialog = false;
      }
      this.popAB = false;
    },
    countTime(t) {
      return (
        Number(t.split(":")[0]) * 3600 +
        Number(t.split(":")[1]) * 60 +
        Number(t.split(":")[2])
      );
    },
    genPoppupMsg(type) {
      if (this.stepDirection % 2 == 0) {
        if (this.currentYear == 0) {
          if (type == "A") {
            this.popMsg =
              this.eqLangLabels[this.$vuetify.lang.current].popup_window;
          } else {
            this.popMsg =
              this.eqLangLabels[this.$vuetify.lang.current].msg_response_43;
          }
        } else {
          if (type == "A" && this.currentYear == 0.5) {
            this.popMsg =
              this.eqLangLabels[this.$vuetify.lang.current].popup_window;
          } else {
            this.popMsg =
              this.eqLangLabels[this.$vuetify.lang.current].msg_response_41 +
              (10 - this.currentYear) +
              this.eqLangLabels[this.$vuetify.lang.current].msg_response_42;
          }
        }
      } else {
        if (this.currentYearB == 0) {
          this.popMsg =
            this.eqLangLabels[this.$vuetify.lang.current].msg_response_53;
        } else {
          this.popMsg =
            this.eqLangLabels[this.$vuetify.lang.current].msg_response_51 +
            (20 - this.currentYearB) +
            this.eqLangLabels[this.$vuetify.lang.current].msg_response_52;
        }
      }
      if (type != "A" && type != "B") {
        console.log("hihihi .....");
        this.popAB = true;
      }
      this.popupDialog = true;
    },
    reset() {
      this.resets++;
      this.slide = 1;
      this.currentYear = 10;
      this.step = 0;
      this.currentYearB = 10;
      this.stepB = 0;
      this.stepDirection = 0;

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
          // this.drawLine(
          //   "canvas2",
          //   this.$refs.table2.offsetWidth,
          //   20,
          //   this.$refs.table2.offsetWidth,
          //   10,
          //   0
          // );
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
      if (type === "A") {
        if (this.slide === 1) {
          if (this.step === 0) {
            this.currentYear = this.currentYear - 10;
          } else if (this.step === 1) {
            this.genPoppupMsg(type);
            // this.popA_to_B = true;
            // this.popupDialog = true;
            this.slide = 2;
            this.stepDirection++;
          } else if (this.step === 2) {
            this.currentYear--;
          } else if (this.step >= 3) {
            if (this.stepDirection >= 1 && this.currentYear === 0.5) {
              // this.popA_to_B = true;
              // this.popupDialog = true;
              this.genPoppupMsg(type);
              console.log("here......");
              this.slide = 2;
              this.stepDirection++;
            }
            if (
              (this.currentYear > 0 && this.currentYear <= 1) ||
              (this.currentYear > 9 && this.currentYear <= 10) ||
              this.currentYear % 1 === 0.5 ||
              this.selected[this.selected.length - 1] != type
            ) {
              this.currentYear = this.currentYear - 0.5;
            } else if (this.currentYear === 0) {
              // this.popA_to_B = true;
              // this.popupDialog = true;
              this.genPoppupMsg(type);
              this.slide = 2;
              this.stepDirection++;
            } else {
              this.currentYear--;
            }
          }
        } else if (this.slide === 2) {
          if (this.stepDirection <= 1) {
            if (this.stepB === 1) {
              this.currentYearB = this.currentYearB - 5;
            } else if (this.stepB === 2) {
              this.currentYearB--;
            } else if (this.stepB >= 3) {
              if (
                (this.currentYearB > 0 && this.currentYearB <= 1) ||
                (this.currentYearB > 9 && this.currentYearB <= 10) ||
                this.currentYearB % 1 === 0.5 ||
                this.selected[this.selected.length - 1] != type
              ) {
                this.currentYearB = this.currentYearB - 0.5;
              } else if (this.currentYearB === 0) {
                return;
              } else {
                this.currentYearB--;
              }
            }
          } else {
            if (this.stepB === 0) {
              this.stepB++;
              return;
            } else {
              if (
                (this.currentYearB > 0 && this.currentYearB <= 1) ||
                (this.currentYearB > 9 && this.currentYearB <= 10) ||
                this.currentYearB % 1 === 0.5 ||
                this.selected[this.selected.length - 1] != type
              ) {
                this.currentYearB = this.currentYearB - 0.5;
              } else if (this.currentYearB === 0) {
                return;
              } else {
                this.currentYearB--;
              }
            }
          }
        }
      } else if (type === "B") {
        if (this.slide === 1) {
          if (this.step === 0) {
            return;
          } else if (this.step === 1) {
            this.currentYear = this.currentYear + 5;
          } else if (this.step === 2) {
            this.currentYear++;
          } else if (this.step >= 3) {
            if (
              (this.currentYear >= 0 && this.currentYear < 1) ||
              (this.currentYear >= 9 && this.currentYear < 10) ||
              this.currentYear % 1 === 0.5 ||
              this.selected[this.selected.length - 1] != type
            ) {
              this.currentYear = this.currentYear + 0.5;
            } else if (this.currentYear >= 10) {
              return;
            } else {
              this.currentYear++;
            }
          }
        } else if (this.slide === 2) {
          if (this.currentYearB >= 10) {
            this.slide = 1;
            this.stepDirection++;
            this.stepB = 0;
            this.currentYear = this.currentYear + 0.5;
          } else {
            if (this.stepDirection <= 1) {
              if (this.stepB >= 3) {
                if (
                  (this.currentYearB >= 0 && this.currentYearB < 1) ||
                  (this.currentYearB >= 9 && this.currentYearB < 10) ||
                  this.currentYearB % 1 === 0.5 ||
                  this.selected[this.selected.length - 1] != type
                ) {
                  this.currentYearB = this.currentYearB + 0.5;
                } else {
                  this.currentYearB++;
                }
              } else {
                this.currentYearB++;
              }
            } else {
              if (
                (this.currentYearB >= 0 && this.currentYearB < 1) ||
                (this.currentYearB >= 9 && this.currentYearB < 10) ||
                this.currentYearB % 1 === 0.5 ||
                this.selected[this.selected.length - 1] != type
              ) {
                this.currentYearB = this.currentYearB + 0.5;
              } else {
                this.currentYearB++;
                console.log("here ...");
              }
            }
          }
        }
      } else {
        this.genPoppupMsg(type);
        // this.popupDialog = true;
      }

      // this.clearCanvas('canvas1')
      if (type != "A" && type != "B") {
        // console.log("type: "+type)
        // console.log("hi--------")
        return false;
      }
      this.selected.push(type);
      this.step++;
      if (this.slide === 2) {
        this.stepB++;
      }
      // console.log("AB not executed ...")
      if (this.currentYear >= 0 && this.slide === 1) {
        this.$nextTick(() => {
          this.drawLine(
            "canvas1",
            this.$refs.table1.offsetWidth,
            20,
            (this.$refs.table1.offsetWidth / this.topYear) * this.currentYear,
            10,
            0
          );
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

          // console.log(this.cStyle1);
          console.log("sytle -----------");

          // this.drawLine(
          //   "canvas2",
          //   this.$refs.table2.offsetWidth,
          //   20,
          //   this.$refs.table2.offsetWidth,
          //   10,
          //   0
          // );
        });
      }
      if (this.currentYearB >= 0 && this.slide === 2) {
        this.$nextTick(() => {
          this.drawLine(
            "canvas3",
            this.$refs.table3.offsetWidth,
            20,
            (this.$refs.table3.offsetWidth / this.topYearB) * this.currentYearB,
            10,
            0
          );
          this.drawLine(
            "canvas4",
            0,
            20,
            this.$refs.table4.offsetWidth/2,
            20,
             this.$refs.table4.offsetWidth/2
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
          this.drawLine(
            "canvas5",
            this.$refs.table4.offsetWidth / 2 ,
            20,
            this.$refs.table4.offsetWidth,
            20,
            this.$refs.table4.offsetWidth/2 -5
          );
        });
      }
    },

    drawLine(cvs, startx, starty, endx, endy,cvswidth) {
      //获取画板
      var canvas = document.getElementById(cvs);

      if (canvas == null) return false;

      canvas.height = endy + 5;
      canvas.width = cvswidth;

      //获取画笔
      var ctx = canvas.getContext("2d");

      drawLineWithArrows(startx, starty, endx, endy, 5, 8, true, true);

      // x0,y0: the line's starting point
      // x1,y1: the line's ending point
      // width: the distance the arrowhead perpendicularly extends away from the line
      // height: the distance the arrowhead extends backward from the endpoint
      // arrowStart: true/false directing to draw arrowhead at the line's starting point
      // arrowEnd: true/false directing to draw arrowhead at the line's ending point
      function drawLineWithArrows(
        x0,
        y0,
        x1,
        y1,
        aWidth,
        aLength,
        arrowStart,
        arrowEnd
      ) {
        var dx = x1 - x0;
        var dy = y1 - y0;
        var angle = Math.atan2(dy, dx);
        var length = Math.sqrt(dx * dx + dy * dy);
        //
        ctx.translate(x0, y0);
        ctx.rotate(angle);
        ctx.beginPath();
        ctx.moveTo(0, 0);
        ctx.lineTo(length, 0);
        if (arrowStart) {
          ctx.moveTo(aLength, -aWidth);
          ctx.lineTo(0, 0);
          ctx.lineTo(aLength, aWidth);
        }
        if (arrowEnd) {
          ctx.moveTo(length - aLength, -aWidth);
          ctx.lineTo(length, 0);
          ctx.lineTo(length - aLength, aWidth);
        }
        //
        ctx.stroke();
        ctx.setTransform(1, 0, 0, 1, 0, 0);
      }
    },
    start() {
      // this.startTime = new Date();
      this.itemStartTime = new Date();
    },
    end() {
      this.endTime = new Date();
      this.usedTime = this.startTime
        ? this.getFormatTime(this.startTime, this.endTime)
        : "00:00:00";
      // console.log(this.usedTime)
      this.itemEndTime = new Date();
      this.itemUsedTime = this.itemStartTime
        ? this.getFormatTime(this.itemStartTime, this.itemEndTime)
        : "00:00:00";
    },
    getFormatTime(stime, etime) {
      //计算小时数
      let diffTime1 = (etime - stime) % (24 * 3600 * 1000);
      let hours = Math.floor(diffTime1 / (3600 * 1000));
      //计算相差分钟数
      let diffTime2 = diffTime1 % (3600 * 1000);
      let minutes = Math.floor(diffTime2 / (60 * 1000));
      //计算相差秒数
      let diffTime3 = diffTime2 % (60 * 1000);
      let seconds = Math.round(diffTime3 / 1000);

      if (hours < 10) {
        hours = "0" + hours;
      }
      if (minutes < 10) {
        minutes = "0" + minutes;
      }
      if (seconds < 10) {
        seconds = "0" + seconds;
      }

      return hours + ":" + minutes + ":" + seconds;
    },
    getUsedTime() {
      setInterval(this.end, 1000);
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
      this.$emit("cUpdateItem", this.ttoAnswer);
    },
    closeDialog() {
      this.popupDialog = false;
      this.popA = false;
      this.popB = false;
      this.popA_to_B = false;
      this.popAZero = false;
      this.popBFull = false;
    },
    drawmyLine() {
      const canvas = document.getElementById("mycanvas");
      const ctx = canvas.getContext("2d");

      ctx.moveTo(90, 130);
      ctx.lineTo(95, 25);
      ctx.lineTo(150, 80);
      ctx.lineTo(205, 25);
      ctx.lineTo(210, 130);
      ctx.lineWidth = 15;
      ctx.stroke();
    },
  },
  created() {
    // this.getCurrentTime();
    // console.log("created tto")
    this.start();
    // this.startTime = new Date();
    this.getUsedTime();
    this.drawmyLine();
  },
  beforeDestroy() {
    // clearInterval(this.currentTime);
    clearInterval(this.startTime);
    clearInterval(this.endTime);
    clearInterval(this.usedTime);
    clearInterval(this.itemStartTime);
    clearInterval(this.itemEndTime);
    clearInterval(this.itemUsedTime);
  },
  mounted() {
    this.drawLine("canvas1", 0, 15, this.$refs.table1.offsetWidth, 15,this.$refs.table1.offsetWidth);
    this.drawLine("canvas11", 0, 15, this.$refs.table11.offsetWidth, 15,this.$refs.table11.offsetWidth);
    this.drawLine("canvas2", 0, 15, this.$refs.table2.offsetWidth, 15,this.$refs.table2.offsetWidth);
    this.drawLine("canvas12", 0, 15, this.$refs.table12.offsetWidth, 15,this.$refs.table12.offsetWidth);
    this.$refs.tenyear.style.width = this.$refs.table2.offsetWidth + "px";
    this.$refs.fixdiv.style.width = this.$refs.table1.offsetWidth + "px";
  },
  computed: {
    allContent: function () {
      return function (year) {
        var arr = [];
        for (var i = 1; i <= 4 * year; i++) {
          arr.push(i);
        }
        return arr;
      };
    },
    ...mapState(["userInfo", "examType", "qVersion", "eqLangLabels"]),
  },
};
</script>

<style lang="scss" scoped>
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
