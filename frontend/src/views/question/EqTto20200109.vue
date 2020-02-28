<template>
  <v-container class="grey lighten-5" fluid>
    <v-card justify="center" align="start">
      <v-card-title v-show="true">
        <v-row>
          <v-col>
            <v-alert dense type="info">{{ eqLangLabels[$vuetify.lang.current].question }}</v-alert>
            <!-- {{newBlock.split("*")}} -->
          </v-col>
        </v-row>
        <!-- <v-spacer></v-spacer>
        <span color="grey">总共用时： {{usedTime}}</span>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <span color="grey">本题用时： {{itemUsedTime}}</span>-->
      </v-card-title>
      <!-- <v-divider></v-divider> -->
      <v-card-text>
        <v-row>
          <v-col cols="3" class="px-8">
            <v-row justify="end" class="pt-8">
              <v-btn class="primary" @click="chooseAnswer('A')" fab large dark>A</v-btn>
            </v-row>
            <v-row justify="end" class="my-2">
              <v-btn class="yellow darken-3" @click="chooseAnswer('AB')" large dark>A & B</v-btn>
            </v-row>
            <v-row justify="end" class="my-2">
              <v-btn class="purple" @click="chooseAnswer('B')" fab large dark>B</v-btn>
            </v-row>
            <v-row justify="end" class="my-2">
              <v-btn class="teal" v-if="step>0" @click="reset">
                <v-icon>refresh</v-icon>
              </v-btn>
            </v-row>
          </v-col>
          <v-col cols="9" class="px-8" v-if="slide==1">
            <!-- <v-row v-if="showDetail" justify="start">
              <span class="display-0">当前SLIDE： {{ slide }}</span>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              <span
                class="display-0"
              >当前Direction： {{ stepDirection }}</span>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              <span class="display-0">重置次数： {{ resets }}</span>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              <span class="display-0">当前步骤：{{step}}</span>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              <span class="display-0">当前步骤B：{{stepB}}</span>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              <span
                class="display-0"
              >当前年A： {{ currentYear }}</span>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              <span
                class="display-0"
              >当前年B： {{ currentYearB }}</span>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              <span
                class="display-0"
              >当前题目： {{ block.name }}</span>
            </v-row>-->
            <v-row justify="start" align="center">
              <div>
                <div :style="cStyle1" style="text-align: center">{{Math.floor(currentYear) + eqLangLabels[$vuetify.lang.current].years + (((currentYear%1)*12 != 0)?(',' + (currentYear%1)*12 + eqLangLabels[$vuetify.lang.current].months):'') }} </div>
                <canvas id="canvas1" ref="canvas1"></canvas>
              </div>
              <table border="1" cellspacing="0" cellpadding="0" ref="table1">
                <tr style="height: 50px">
                  <td
                    v-for="item in allContent(topYear)"
                    :key="item"
                    style="text-align: center; width: 24px"
                    :class="item<=4*currentYear?'light-green lighten-1':''"
                  ></td>
                </tr>
              </table>
            </v-row>
            <v-row justify="start" align="center" class="pt-12 mt-12">
              <table border="1" cellspacing="0" cellpadding="0" ref="table2">
                <tr style="height: 50px">
                  <td
                    v-for="item in allContent(topYear)"
                    :key="item"
                    style="text-align: center; width: 24px"
                    class="blue lighten-2"
                  ></td>
                </tr>
              </table>
              <div>
                <canvas id="canvas2" ref="canvas2"></canvas>
              </div>
            </v-row>
          </v-col>
          <v-col cols="9" class="px-8" v-if="slide==2">
            <v-row justify="start">
              <div>
                <div :style="cStyle3" style="text-align: center">{{Math.floor(currentYearB) + eqLangLabels[$vuetify.lang.current].years + (((currentYearB%1)*12 != 0)?(',' + (currentYearB%1)*12 + eqLangLabels[$vuetify.lang.current].months):'') }}</div>
                <canvas id="canvas3" ref="canvas3"></canvas>
              </div>
              <table border="1" cellspacing="0" cellpadding="0" ref="table3">
                <tr style="height: 50px">
                  <td
                    v-for="item in allContent(topYearB)"
                    :key="item"
                    style="text-align: center; width: 16px"
                    :class="item<=4*currentYearB?'light-green lighten-1':''"
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
                    :class="item<=40?'light-green lighten-1':'blue lighten-2'"
                  ></td>
                </tr>
              </table>
              <div>
                <canvas id="canvas4" ref="canvas4"></canvas>
                <canvas id="canvas5" ref="canvas5"></canvas>
              </div>
            </v-row>
          </v-col>
        </v-row>
        <v-row justify="center" align="center" v-if="slide==1 &&  block.source_text ">
          <v-col cols="6">
            <v-row>
              <div class="message-box pa-5 mt-5" style="margin-left: 200px; text-align: left">
                <div v-for="msg in  block.source_text.split('*')" :key="msg.key">
                  <li v-if="msg != ''">
                    <span>{{msg}}</span>
                  </li>
                </div>
              </div>
            </v-row>
          </v-col>
        </v-row>

        <v-row justify="center" align="center" v-if="slide==2">
          <v-col cols="6">
            <v-row>
              <div class="message-box-1 pa-5 mt-5" style="margin-left: 200px;text-align:left">
                <span>完全健康</span>
              </div>
            </v-row>
          </v-col>
        </v-row>
        <v-row justify="center" align="center" v-if="slide==2 &&  block.source_text">
          <v-col cols="6">
            <v-row>
              <div class="message-box-2 pa-5 mt-5" style="margin-left: 200px;text-align:left">
                <div v-for="msg in block.source_text.split('*')" :key="msg.key">
                  <li v-if="msg != ''">
                    <span>{{msg}}</span>
                  </li>
                </div>
              </div>
            </v-row>
          </v-col>
        </v-row>
      </v-card-text>

      <!-- <v-card-text v-if="slide === 2">
        <v-row v-if="showDetail">
          <v-col>
            <span class="display-0">当前SLIDE： {{ slide }}</span>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <span
              class="display-0"
            >当前Direction： {{ stepDirection }}</span>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <span class="display-0">重置次数： {{ resets }}</span>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <span class="display-0">当前步骤：{{step}}</span>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <span class="display-0">当前步骤B：{{stepB}}</span>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <span
              class="display-0"
            >当前年A： {{ currentYear }}</span>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <span
              class="display-0"
            >当前年B： {{ currentYearB }}</span>
          </v-col>
        </v-row>
      </v-card-text>-->
      <v-divider></v-divider>
      <!-- <v-card-actions>
        <v-btn class="green" @click="start">Start</v-btn>
        <v-spacer></v-spacer>
        <v-btn class="primary" @click="chooseAnswer('A')">A</v-btn>
        <v-btn class="yellow darken-3" @click="chooseAnswer('AB')">A & B</v-btn>
        <v-btn class="purple" @click="chooseAnswer('B')">B</v-btn>
        <v-btn class="teal" v-if="step>0" @click="reset">
          <v-icon>refresh</v-icon>
        </v-btn>
        <v-btn class="yellow" @click="showDetail=!showDetail">
          <v-icon>mdi-details</v-icon>
        </v-btn>
        <v-spacer></v-spacer>
      </v-card-actions>-->
    </v-card>
    <v-row>
      <v-dialog v-model="popupDialog" persistent max-width="600">
        <v-card class="pt-5 yellow lighten-4">
          <v-card-text class="display-1" style="text-indent:2em;">
            <span
              v-if="popA"
            >{{ eqLangLabels[$vuetify.lang.current].msg_response_41 + currentYear + eqLangLabels[$vuetify.lang.current].msg_response_42}}</span>
            <span v-if="popA_to_B">{{ eqLangLabels[$vuetify.lang.current].popup_window }}</span>
            <span v-if="popAZero">{{ eqLangLabels[$vuetify.lang.current].msg_response_43 }}</span>
            <span v-if="popBFull">{{ eqLangLabels[$vuetify.lang.current].msg_response_53 }}</span>
            <span
              v-if="popB"
            >{{ eqLangLabels[$vuetify.lang.current].msg_response_51 + currentBYear + eqLangLabels[$vuetify.lang.current].msg_response_52}}</span>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="light-green darken-3"
              @click="closeDialog"
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
import { mapState } from "vuex";
export default {
  name: "EqTto",
  props: ["block", "startTime"],
  data: () => ({
    cStyle1: "",
    cStyle3: "",
    showDetail: false,
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
    popA: false,
    popB: false,
    popA_to_B: false,
    popAZero: false,
    popBFull: false
    // newBlock: ""
  }),

  methods: {
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
            this.currentYear
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
            this.currentYearB
          );
        }
      });
    },
    chooseAnswer(type) {
      if (type === "A") {
        // alert("A");
        // this.popA = true;
        // this.popupDialog = true;
        if (this.slide === 1) {
          if (this.step === 0) {
            this.currentYear = this.currentYear - 10;
          } else if (this.step === 1) {
            // alert(this.bAlertText);
            this.popA_to_B = true;
            this.popupDialog = true;
            this.slide = 2;
            this.stepDirection++;
          } else if (this.step === 2) {
            this.currentYear--;
          } else if (this.step >= 3) {
            if (this.stepDirection >= 1 && this.currentYear === 0.5) {
              // alert(this.bAlertText);
              this.popA_to_B = true;
              this.popupDialog = true;
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
              // alert(this.bAlertText);
              this.popA_to_B = true;
              this.popupDialog = true;
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
        // alert("B");
        // this.popB = true;
        // this.popupDialog = true;
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
        if (this.stepDirection % 2 == 0) {
          if (this.currentYear == 0) {
            alert(
              this.eqLangLabels[this.$vuetify.lang.current].msg_response_43
            );
          } else {
            alert(
              this.eqLangLabels[this.$vuetify.lang.current].msg_response_41 +
                (10 - this.currentYear) +
                this.eqLangLabels[this.$vuetify.lang.current].msg_response_42
            );
          }
        } else {
          if (this.currentYearB == 0) {
            alert(
              this.eqLangLabels[this.$vuetify.lang.current].msg_response_53
            );
          } else {
            alert(
              this.eqLangLabels[this.$vuetify.lang.current].msg_response_51 +
                (20 - this.currentYearB) +
                this.eqLangLabels[this.$vuetify.lang.current].msg_response_52
            );
          }
        }

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
          tto_value: ttoValue,
          used_time: this.itemUsedTime,
          composite_switches: this.stepDirection,
          resets: this.resets,
          number_of_moves: this.step,
          block: this.block.block,
          version: this.qVersion
        };
        this.ttoAnswer = answerObj;

        // console.log("本题用时：" + this.itemUsedTime);
        this.itemStartTime = new Date();
        this.itemEndTime = 0;
        this.itemUsedTime = "00:00:00";
        this.getUsedTime();
        // this.reset();
        //通过改变父组件的值
        this.updateItem();
      }
      this.selected.push(type);
      this.step++;
      if (this.slide === 2) {
        this.stepB++;
      }

      // this.clearCanvas('canvas1')
      if (type != "A" && type != "B") {
        // console.log("type: "+type)
        return false;
      }
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
            this.currentYear
          );

          console.log(this.cStyle1)
          this.drawLine(
            "canvas2",
            this.$refs.table2.offsetWidth,
            20,
            this.$refs.table2.offsetWidth,
            10,
            0
          );
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
            this.$refs.table4.offsetWidth / 2,
            20,
            this.$refs.table4.offsetWidth / 2,
            10,
            0
          );
          this.cStyle3 = this.getStyle(
            this.$refs.table3.offsetWidth,
            this.topYearB,
            this.currentYearB
          );
          this.drawLine(
            "canvas5",
            this.$refs.table4.offsetWidth / 2,
            20,
            this.$refs.table4.offsetWidth / 2,
            10,
            0
          );
        });
      }
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
        paddingRight = paddingRight-30
      }
      console.log
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
    }
  },
  created() {
    // this.getCurrentTime();
    // console.log("created tto")
    this.start();
    // this.startTime = new Date();
    this.getUsedTime();
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
    this.drawLine(
      "canvas1",
      this.$refs.table1.offsetWidth,
      20,
      this.$refs.table1.offsetWidth,
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
    // console.log(this.$refs.table1.getBoundingClientRect());
    // console.log("EqTto ....");

    // console.log("-----------------------");
    // var mystr = "apple";
    // console.log(this.block);

    // if (this.block.source_text) {
    //   this.newBlock = this.block.source_text;
    // }
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
</style>