<template>
  <div class="grey lighten-5" style="width:1600px; margin:auto">
    <v-card justify="center" align="start">
      <v-card-title v-show="true">
        <v-row>
          <v-col>
            <v-alert dense type="info">哪一个选择比较好，生命A、生命B，还是它们大致相同？</v-alert>
          </v-col>
        </v-row>
      </v-card-title>
      <v-card-text>
        <v-row justify="center" align="center">
          <!-- 调整这里 -->
          <div style="position: relative;width:100%;height:40px;background:#ffffff">
            <div
              style="background:#92d050;padding:10px 10px;width:200px;border-radius: 15px;position:absolute;right:150px;"
            >
              完全健康
              <v-icon
                style="color:#92d050;font-size:5rem; position: absolute;right:120px; z-index:98; top:5px;"
              >mdi-menu-down</v-icon>
            </div>

            <!--新增弹窗-->
            <v-expand-transition>
              <div
                id="alertbox"
                style="position: absolute;width:300px;height:240px;top:160px;right:180px; z-index:99"
                v-show="isAppend"
              >
                <div
                  style="width:100px;height:52px;background: #2E7D32;position:absolute;top:-66px;right:1px;border:3px solid red;opacity: 0.7;"
                  class="dynamic-icon"
                ></div>
                <div
                  style="position:relative;width:300px;height:240px;background: grey;padding:10px;border-radius: 15px; border:3px solid red;;opacity: 0.7;"
                >
                  <v-icon
                    style="color: red;font-size:5rem; position: absolute;right:20px;top:-50px;"
                  >mdi-menu-up</v-icon>
                </div>
                <div
                  style="text-align: center;width:280px;position:absolute;top:10px;right:10px;background:#ffffff"
                >
                  <table border="1" cellspacing="0" cellpadding="0" style="width:100%">
                    <tr style="height: 50px;">
                      <td
                        :class="(indexList[itemIndex.length] >= 906 || itemIndex.length == 15)?'green darken-1':''"
                        style="text-align: center; width: 25%;"
                      >
                        <span
                          v-if="indexList[itemIndex.length] >= 906 || itemIndex.length == 15"
                        >9年6个月</span>
                      </td>
                      <td
                        :class="(indexList[itemIndex.length] >= 909 || itemIndex.length == 15)?'green darken-1':''"
                        style="text-align: center; width: 25%;"
                      >
                        <span
                          v-if="indexList[itemIndex.length] >= 909 || itemIndex.length == 15"
                        >9年9个月</span>
                      </td>
                      <td
                        :class="(indexList[itemIndex.length] >= 910 || itemIndex.length == 15)?'green darken-1':''"
                        style="text-align: center; width: 25%;"
                      >
                        <span
                          v-if="indexList[itemIndex.length] >= 910 || itemIndex.length == 15"
                        >9年10个月</span>
                      </td>
                      <td
                        :class="(indexList[itemIndex.length] >= 911 || indexList[itemIndex.length - 1] == 911)?'green darken-1':''"
                        style="text-align: center; width: 25%;"
                      >
                        <span
                          v-if="indexList[itemIndex.length] >= 911 || indexList[itemIndex.length - 1] == 911"
                        >9年11个月</span>
                      </td>
                    </tr>
                  </table>

                  <table border="0" cellspacing="0" cellpadding="0" style="width:100%">
                    <tr style="height: 100px;">
                      <td
                        style="text-align: center;width:25%"
                        :class="isSelected(906,'A') == -1?'dynamic-icon':''"
                      >
                        <button
                          type="button"
                          @click="selectItem(906, 'A')"
                          class="v-icon notranslate py-1 v-icon--link mdi theme--light"
                          :class="
                          isSelected(906, 'A') == -1
                            ? ((indexList[itemIndex.length] >= 906 || itemIndex.length == 15)?'mdi-arrow-up-bold grey--text':'')
                            : (isSelected(906, 'A') == 1
                            ? 'mdi-arrow-up-bold green--text'
                            : 't')
                        "
                          style="width:100%"
                        ></button>
                        <button
                          @click="selectItem(906, 'AB')"
                          type="button"
                          class="v-icon notranslate py-1 v-icon--link mdi theme--light"
                          :class="
                          isSelected(906, 'AB') == -1
                            ? ((indexList[itemIndex.length] >= 906 || itemIndex.length == 15)?'mdi-view-stream grey--text':'')
                            : (isSelected(906, 'AB') == 1
                            ? 'mdi-view-stream green--text'
                            : 't')
                        "
                          style="font-size: 36px;width:100% "
                        ></button>
                        <button
                          @click="selectItem(906, 'B')"
                          type="button"
                          class="v-icon notranslate py-1 v-icon--link mdi theme--light"
                          :class="
                          isSelected(906, 'B') == -1
                            ? ((indexList[itemIndex.length] >= 906 || itemIndex.length == 15)?'mdi-arrow-down-bold  grey--text':'')
                            : (isSelected(906, 'B') == 1
                            ? 'mdi-arrow-down-bold green--text'
                            : 't')
                        "
                          style="width:100%"
                        ></button>
                      </td>
                      <td
                        style="text-align: center;width:25%"
                        :class="isSelected(909,'A') == -1?'dynamic-icon':''"
                      >
                        <button
                          type="button"
                          @click="selectItem(909, 'A')"
                          class="v-icon notranslate py-1 v-icon--link mdi theme--light"
                          :class="
                          isSelected(909, 'A') == -1
                            ? ((indexList[itemIndex.length] >= 909 || itemIndex.length == 15)?'mdi-arrow-up-bold grey--text':'')
                            : (isSelected(909, 'A') == 1
                            ? 'mdi-arrow-up-bold green--text'
                            : 't')
                        "
                          style="width:100%"
                        ></button>
                        <button
                          type="button"
                          @click="selectItem(909, 'AB')"
                          class="v-icon notranslate py-1 v-icon--link mdi theme--light"
                          :class="
                           isSelected(909, 'AB') == -1
                            ? ((indexList[itemIndex.length] >= 909 || itemIndex.length == 15)?'mdi-view-stream grey--text':'')
                            : (isSelected(909, 'AB') == 1
                            ? 'mdi-view-stream green--text'
                            : 't')
                        "
                          style="font-size: 36px;width:100%"
                        ></button>
                        <button
                          type="button"
                          @click="selectItem(909, 'B')"
                          class="v-icon notranslate py-1 v-icon--link mdi theme--light"
                          :class="
                          isSelected(909, 'B') == -1
                            ? ((indexList[itemIndex.length] >= 909 || itemIndex.length == 15)?'mdi-arrow-down-bold  grey--text':'')
                            : (isSelected(909, 'B') == 1
                            ? 'mdi-arrow-down-bold green--text'
                            : 't')
                        "
                          style="width:100%"
                        ></button>
                      </td>
                      <td
                        style="text-align: center;width:25%"
                        :class="isSelected(910,'A') == -1?'dynamic-icon':''"
                      >
                        <button
                          type="button"
                          @click="selectItem(910, 'A')"
                          class="v-icon notranslate py-1 v-icon--link mdi theme--light"
                          :class="
                          isSelected(910, 'A') == -1
                            ? ((indexList[itemIndex.length] >= 910 || itemIndex.length == 15)?'mdi-arrow-up-bold grey--text':'')
                            : (isSelected(910, 'A') == 1
                            ? 'mdi-arrow-up-bold green--text'
                            : 't')
                        "
                          style="width:100%"
                        ></button>
                        <button
                          type="button"
                          @click="selectItem(910, 'AB')"
                          class="v-icon notranslate py-1 v-icon--link mdi theme--light"
                          :class="
                          isSelected(910, 'AB') == -1
                            ? ((indexList[itemIndex.length] >= 910 || itemIndex.length == 15)?'mdi-view-stream grey--text':'')
                            : (isSelected(910, 'AB') == 1
                            ? 'mdi-view-stream green--text'
                            : 't')
                        "
                          style="font-size: 36px;width:100%"
                        ></button>
                        <button
                          type="button"
                          @click="selectItem(910, 'B')"
                          class="v-icon notranslate py-1 v-icon--link mdi theme--light"
                          :class="
                         isSelected(910, 'B') == -1
                            ? ((indexList[itemIndex.length] >= 910 || itemIndex.length == 15)?'mdi-arrow-down-bold  grey--text':'')
                            : (isSelected(910, 'B') == 1
                            ? 'mdi-arrow-down-bold green--text'
                            : 't')
                        "
                          style="width:100%"
                        ></button>
                      </td>

                      <td
                        style="text-align: center;width:25%"
                        :class="isSelected(911,'A') == -1?'dynamic-icon':''"
                      >
                        <button
                          type="button"
                          @click="selectItem(911, 'A')"
                          class="v-icon notranslate py-1 v-icon--link mdi theme--light blue--text"
                          :class="
                          isSelected(911, 'A') == -1
                            ? ((indexList[itemIndex.length] >= 911 || indexList[itemIndex.length - 1] == 911)?'mdi-arrow-up-bold grey--text':'')
                            : (isSelected(911, 'A') == 1
                            ? 'mdi-arrow-up-bold green--text'
                            : 't')
                        "
                          style="width:100%"
                        ></button>
                        <button
                          type="button"
                          @click="selectItem(911, 'AB')"
                          class="v-icon notranslate py-1 v-icon--link mdi theme--light blue--text"
                          :class="
                          isSelected(911, 'AB') == -1
                            ? ((indexList[itemIndex.length] >= 911 || indexList[itemIndex.length - 1] == 911)?'mdi-view-stream grey--text':'')
                            : (isSelected(911, 'AB') == 1
                            ? 'mdi-view-stream green--text'
                            : 't')
                        "
                          style="font-size: 36px;width:100%"
                        ></button>
                        <button
                          type="button"
                          @click="selectItem(911, 'B')"
                          class="v-icon notranslate py-1 v-icon--link mdi theme--light"
                          :class="
                           isSelected(911, 'B') == -1
                            ? ((indexList[itemIndex.length] >= 911 || indexList[itemIndex.length - 1] == 911)?'mdi-arrow-down-bold  grey--text':'')
                            : (isSelected(911, 'B') == 1
                            ? 'mdi-arrow-down-bold green--text'
                            : 't')
                        "
                          style="width:100%"
                        ></button>
                      </td>
                    </tr>
                  </table>

                  <table border="1" cellspacing="0" cellpadding="0" style="width:100%">
                    <tr style="height: 50px;">
                      <td class="blue lighten-3" style="text-align: center; width: 24px;">10年</td>
                    </tr>
                  </table>
                </div>
              </div>
            </v-expand-transition>
          </div>
          <v-col cols="2">
            <v-row
              justify="center"
              align="center"
              class="font-weight-bold"
              :class="uLarge ? 'headline grey--text text--darken-4' : 'title'"
            >
              <v-btn text @click="selectItem(indexList[itemList.length], 'A')">
                <span
                  class="font-weight-bold"
                  :class="uLarge ? 'headline grey--text text--darken-4' : 'title'"
                >偏好A</span>
              </v-btn>
            </v-row>
          </v-col>
          <v-col cols="10">
            <v-row></v-row>
            <v-row justify="center" align="center">
              <div
                ref="div1"
                :style="style1"
                style="width: 1002.22px;text-align: right"
              >{{ currentYear }}年</div>
              <canvas id="canvas1" ref="canvas1"></canvas>
            </v-row>
            <v-row justify="center" align="center">
              <table border="1" cellspacing="0" cellpadding="0" ref="table1">
                <tr style="height: 50px">
                  <td
                    v-for="item in 4 * topYear"
                    :key="item"
                    style="text-align: center; width: 24px"
                    :class="
                      isAppend?(parseInt((item - 1) / 4) % 2 == 1
                          ? 'green lighten-3'
                          : 'green darken-1'):((item <= itemIndex[itemIndex.length - 1] - 5 ||
                      itemIndex.length == 0)
                        ? (parseInt((item - 1) / 4) % 2 == 1
                          ? 'green lighten-3'
                          : 'green darken-1')
                        : '')
                    "
                  ></td>
                </tr>
              </table>
            </v-row>
          </v-col>
        </v-row>

        <v-row justify="center" align="center">
          <v-col cols="2">
            <v-row
              justify="center"
              align="center"
              class="font-weight-bold"
              :class="eLarge ? 'headline grey--text text--darken-4' : 'title'"
            >
              <v-btn text @click="selectItem(indexList[itemList.length], 'AB')">
                <span
                  class="font-weight-bold"
                  :class="eLarge ? 'headline grey--text text--darken-4' : 'title'"
                >A和B大致相同</span>
              </v-btn>
            </v-row>
          </v-col>
          <v-col cols="10">
            <v-row justify="center" align="center">
              <table
                border="0"
                cellspacing="0"
                cellpadding="0"
                ref="table2"
                style="table-layout: fixed"
                height="210"
              >
                <tr style="height: 50px">
                  <td
                    v-for="item in 4 * topYear + 1"
                    :key="item"
                    ref="iconList"
                    style="text-align: center; width: 24px;"
                    :class="isSelected(item,'A') == -1?'dynamic-icon':''"
                    @mouseover="mouseOver(item)"
                    @mouseleave="mouseLeave(item)"
                  >
                    <v-icon
                      v-if="item % 4 == 1"
                      @click="selectItem(item, 'A')"
                      class="py-5"
                      :color="
                        uLarge && item == isMouseOverItem
                          ? 'blue darken-4'
                          : isSelected(item, 'A') == 1
                          ? 'green'
                          : item == isMouseOverItem
                          ? 'blue'
                          : 'grey lighten-1'
                      "
                      ref="upIcon"
                      @mouseover="uLarge = true"
                      @mouseleave="uLarge = false"
                      :large="item == isMouseOverItem && uLarge ? true : false"
                      :disabled="!(isSelected(item, 'A') != 0)"
                    >
                      {{
                      isSelected(item, "A") != 0
                      ? isSelected(item, "A") == -1 &&
                      !(
                      (itemIndex[itemIndex.length - 1] - 4 == item &&
                      itemIndex.length != 0) ||
                      (itemIndex.length == 0) &
                      (item == topYear * 4 + 1)
                      ) &&
                      !(item == 4 * topYear - 1 && isAppend)
                      ? "t"
                      : "mdi-arrow-up-bold"
                      : "t"
                      }}
                    </v-icon>
                    <v-icon
                      v-if="item % 4 == 1"
                      @click="selectItem(item, 'AB')"
                      ref="eqIcon"
                      class="py-5"
                      :color="
                        eLarge && item == isMouseOverItem
                          ? 'blue darken-4'
                          : isSelected(item, 'AB') == 1
                          ? 'green'
                          : item == isMouseOverItem
                          ? 'blue'
                          : 'grey lighten-1'
                      "
                      :disabled="!(isSelected(item, 'AB') != 0)"
                      @mouseover="eLarge = true"
                      @mouseleave="eLarge = false"
                      :large="item == isMouseOverItem && eLarge ? true : false"
                    >
                      {{
                      isSelected(item, "AB") != 0
                      ? isSelected(item, "AB") == -1 &&
                      !(
                      (itemIndex[itemIndex.length - 1] - 4 == item &&
                      itemIndex.length != 0) ||
                      (itemIndex.length == 0) &
                      (item == topYear * 4 + 1)
                      ) &&
                      !(item == 4 * topYear - 1 && isAppend)
                      ? "t"
                      : "mdi-view-stream"
                      : "t"
                      }}
                    </v-icon>
                    <v-icon
                      v-if="item % 4 == 1"
                      @click="selectItem(item, 'B')"
                      class="py-5"
                      ref="dwIcon"
                      :color="
                        dLarge && item == isMouseOverItem
                          ? 'blue darken-4'
                          : isSelected(item, 'B') == 1
                          ? 'green'
                          : item == isMouseOverItem
                          ? 'blue'
                          : 'grey lighten-1'
                      "
                      :disabled="!(isSelected(item, 'B') != 0)"
                      @mouseover="dLarge = true"
                      @mouseleave="dLarge = false"
                      :large="item == isMouseOverItem && dLarge ? true : false"
                    >
                      {{
                      isSelected(item, "B") != 0
                      ? isSelected(item, "B") == -1 &&
                      !(
                      (itemIndex[itemIndex.length - 1] - 4 == item &&
                      itemIndex.length != 0) ||
                      (itemIndex.length == 0) &
                      (item == topYear * 4 + 1)
                      ) &&
                      !(item == 4 * topYear - 1 && isAppend)
                      ? "t"
                      : "mdi-arrow-down-bold"
                      : "t"
                      }}
                    </v-icon>
                  </td>
                </tr>
              </table>
            </v-row>
          </v-col>
        </v-row>

        <v-row justify="center" align="center">
          <v-col cols="2">
            <v-row justify="center" align="center">
              <!-- <div v-for="item in 4 * topYear + 1" :key="item">
                <v-btn
                  text
                  @click="selectItem(item, 'B')"
                  v-if="(itemIndex.length != 0 && item == itemIndex[itemIndex.length-1]-4) || (itemIndex.length == 0 && item == 41)"
                >
                  <span
                    class="font-weight-bold"
                    :class="dLarge ? 'headline grey--text text--darken-4' : 'title'"
                  >偏好B</span>
                </v-btn>
              </div>-->
              <v-btn text @click="selectItem(indexList[itemList.length], 'B')">
                <span
                  class="font-weight-bold"
                  :class="dLarge ? 'headline grey--text text--darken-4' : 'title'"
                >偏好B</span>
              </v-btn>
            </v-row>
          </v-col>
          <v-col cols="10">
            <v-row justify="center" align="center">
              <table border="1" cellspacing="0" cellpadding="0" ref="table3">
                <tr style="height: 50px">
                  <td
                    v-for="item in 4 * topYear"
                    :key="item"
                    style="text-align: center; width: 24px"
                    :class="
                      parseInt((item - 1) / 4) % 2 == 1
                        ? 'blue lighten-3'
                        : 'blue darken-1'
                    "
                  ></td>
                </tr>
              </table>
            </v-row>
            <v-row justify="center" align="center">
              <canvas id="canvas2" ref="canvas2"></canvas>
              <div ref="div2" style="width: 1002.22px;text-align: center">{{ topYear }}年</div>
            </v-row>
          </v-col>
          <!-- 调整这里 -->
          <div style="position: relative;width:100%;height:140px;background:#ffffff">
            <div
              style="background:#5b9bd5;padding:10px 10px;width:300px;border-radius: 25px;position:absolute;left:450px;"
              v-if="block.source_text"
            >
              <v-icon
                style="color:#5b9bd5;font-size:5rem; position: absolute;left:150px; z-index:98; top:-45px;"
              >mdi-menu-up</v-icon>
              <div v-for="msg in block.source_text.split('*')" :key="msg.key">
                <li v-if="msg != ''">
                  <span>{{ msg }}</span>
                </li>
              </div>
            </div>
          </div>
        </v-row>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="primary" @click="reSelect">
          <v-icon large>refresh</v-icon>
        </v-btn>
        <v-btn color="primary" @click="nextQuestion">
          <v-icon large>mdi-arrow-right-circle-outline</v-icon>
        </v-btn>
        <v-spacer></v-spacer>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  data: () => ({
    topYear: 10,
    isMouseOverItem: -1,
    isAppend: false,
    uLarge: false,
    eLarge: false,
    dLarge: false,
    itemList: [],
    itemIndex: [],
    style1: "",
    currentYear: 10,
    nstpttoAnswer: "",
    indexList: [41, 37, 33, 29, 25, 21, 17, 13, 9, 5, 1, 906, 909, 910, 911]
  }),
  props: ["block"],
  methods: {
    selectItem(k, v) {
      console.log(k);
      if (
        !(
          (this.itemIndex.length == 0 && k == this.topYear * 4 + 1) ||
          (this.itemIndex.length > 0 &&
            k == this.itemIndex[this.itemIndex.length - 1] - 4)
        ) &&
        !((k == 906 || k == 909 || k == 910 || k == 911) && this.isAppend)
      ) {
        alert("请从右至左依次按顺序回答！");
        return;
      }
      // 当选项已经选择，单击选项不会再次记录答案
      if (this.isSelected(k, v) == -1) {
        this.itemList.push({
          index: k,
          answer: v,
          page: this.nstpPage
        });
        this.itemIndex.push(k);
        if (this.currentYear > 0) {
          this.currentYear = this.currentYear - 1;
        }
      }
      this.style1 = this.getStyle(
        24.44 * (this.topYear - this.currentYear / 2) * 4
      );
      this.drawLine(
        "canvas1",
        this.$refs.table1.offsetWidth,
        20,
        (this.$refs.table1.offsetWidth / this.topYear) * this.currentYear,
        10,
        0
      );
      console.log(this.itemList);
      // console.log(this.itemIndex);
      // console.log(this.isSelected(k, v));
      // 判断A页面是否回答完成，如果最后一次回答且本次与前面所有都选择A，选择答案后跳转到B页面继续回答持续的11道问题
      var aCount = 0;
      var bCount = 0;
      for (var i = 0; i < this.itemList.length; i++) {
        if (this.itemList[i].answer == "A") {
          aCount++;
        }
        if (this.itemList[i].answer == "B") {
          bCount++;
        }
      }
      // 逻辑2，如果第一次选A，第二次到第11次都选择B或AB，那么问到第11题之后追加一道是否为9.5年的问题
      // console.log(aCount);
      if (
        aCount == 1 &&
        bCount == 10 &&
        this.itemList[0].answer == "A" &&
        this.itemList.length == 11
      ) {
        this.isAppend = true;
        // this.currentYear = 9.5;
        // this.style1 = this.getStyle(
        //   24.44 * (this.topYear - this.currentYear) * 4
        // );
        console.log(this.itemList);
      }
      if (aCount == 11 && this.itemList.length == 11) {
        var arr = [];
        for (var i = 0; i < this.itemList.length; i++) {
          var answerObj = {
            questionid: this.examType.id,
            participant: this.userInfo.participant,
            interviewer: this.userInfo.interviewer,
            item: this.block.name,
            position_of_item: this.block.id,
            select_order: i,
            select_value: this.itemList[i].answer,
            page: 1,
            block: this.block.block,
            version: this.qVersion
          };
          arr.push(answerObj);
        }
        this.nstpttoAnswer = arr;
        // 把第一个页面的答案保存起来
        this.updateItem(this.nstpttoAnswer, false);
        // 切换到第二个页面继续答题
        this.$store.dispatch("setNstpPage", 2);
      }
      console.log(this.itemIndex);
    },
    mouseOver(item) {
      // if (item % 4 == 1) {
      //   console.log(this.$refs.iconList[item - 1]);
      //   // console.log(this.$refs.iconList[item - 1].children[0].className);
      //   let eLenth = this.$refs.iconList[item - 1].children.length;
      //   for (var i = 0; i < eLenth; i++) {
      //       this.$refs.iconList[item - 1].children[i].style.color = "#3F51B5";
      //   }
      // }
      this.isMouseOverItem = item;
    },
    mouseLeave() {
      // if (item % 4 == 1) {
      //   // console.log(this.$refs.iconList[item - 1].children.length);
      //   let eLenth = this.$refs.iconList[item - 1].children.length;
      //   for (var i = 0; i < eLenth; i++) {
      //       this.$refs.iconList[item - 1].children[i].style.color = "#BDBDBD";
      //   }
      // }
      this.isMouseOverItem = -1;
    },
    reSelect() {
      this.topYear = 10;
      this.currentYear = 10;
      this.style1 = "";
      this.isMouseOverItem = -1;
      this.isAppend = false;
      this.uLarge = false;
      this.eLarge = false;
      this.dLarge = false;
      this.itemList = [];
      this.itemIndex = [];
      this.$store.dispatch("setNstpPage", 1);
      this.drawLine(
        "canvas1",
        this.$refs.table1.offsetWidth,
        20,
        this.$refs.table1.offsetWidth,
        10,
        0
      );
    },
    getStyle(w) {
      return "padding-right: " + w + "px;";
    },
    updateItem(arr, next) {
      this.$emit("cUpdateItem", { arr: arr, next: next });
    },
    nextQuestion() {
      // var aCount = 0;
      // for (var i = 1; i < this.itemList.length - 1; i++) {
      //   if (this.itemList[i].answer == "A") {
      //     aCount++;
      //   }
      // }
      if (
        (this.isAppend && this.itemList.length == 15) ||
        (!this.isAppend && this.itemList.length == 11)
      ) {
        var arr = [];
        for (var i = 0; i < this.itemList.length; i++) {
          var answerObj = {
            questionid: this.examType.id,
            participant: this.userInfo.participant,
            interviewer: this.userInfo.interviewer,
            item: this.block.name,
            position_of_item: this.block.id,
            select_order: i,
            select_value: this.itemList[i].answer,
            page: 1,
            block: this.block.block,
            version: this.qVersion
          };
          arr.push(answerObj);
        }
        this.nstpttoAnswer = arr;
        // console.log(this.nstpttoAnswer);
        this.updateItem(this.nstpttoAnswer, true);
        this.$store.dispatch("setNstpPage", 1);
      } else {
        alert("请完成答题步骤才能进行下一步！");
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
    }
  },
  computed: {
    // 判断选项是否选择，选项已选择且为当前答案，返回记录1；选项已选择且非当前单击答案，返回0；选择未选择返回-1.
    isSelected: function() {
      return function(item, answer) {
        for (var i = 0; i < this.itemList.length; i++) {
          if (
            this.itemList[i].index == item &&
            this.itemList[i].answer != answer
          ) {
            return 0;
          }
          if (
            this.itemList[i].index == item &&
            this.itemList[i].answer == answer
          ) {
            return 1;
          }
        }
        return -1;
      };
    },
    ...mapState([
      "userInfo",
      "examType",
      "qVersion",
      "eqLangLabels",
      "nstpPage"
    ])
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
    this.style1 = this.getStyle(
      24.44 * (this.topYear - this.currentYear / 2) * 4
    );
  }
};
</script>


<style lang="scss" scoped>
@keyframes fade {
  from {
    opacity: 1;
  }
  50% {
    opacity: 0.4;
  }
  to {
    opacity: 1;
  }
}

@-webkit-keyframes fade {
  from {
    opacity: 1;
  }
  50% {
    opacity: 0.4;
  }
  to {
    opacity: 1;
  }
}
.dynamic-icon {
  color: #fff;
  // font-size: 15px;
  animation: fade 600ms infinite;
  -webkit-animation: fade 600ms infinite;
}
</style>