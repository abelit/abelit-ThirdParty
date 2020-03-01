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
          <v-col cols="2">
            <v-row
              justify="center"
              align="center"
              class="font-weight-bold"
              :class="uLarge?'headline blue--text text--darken-4':'title'"
            >偏好A</v-row>
          </v-col>
          <v-col cols="10">
            <v-row justify="center" align="center">
              <table border="1" cellspacing="0" cellpadding="0" ref="table1">
                <tr style="height: 50px">
                  <td
                    v-for="item in 8 * topYear"
                    :key="item"
                    style="text-align: center; width: 16px"
                    :class="((item<=itemIndex[itemIndex.length-1]-1) || itemIndex.length == 0)?(item<topYear*8/2+1?(parseInt((item - 1) / 4) % 2 == 1 ? 'green lighten-3' : 'green darken-1'):''):''"
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
              :class="eLarge?'headline blue--text text--darken-4':'title'"
            >A和B大致相同</v-row>
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
                    v-for="item in 8 * topYear + 1"
                    :key="item"
                    ref="iconList"
                    style="text-align: center; width: 16px;"
                    @mouseover="mouseOver(item)"
                    @mouseleave="mouseLeave(item)"
                  >
                    <v-icon
                      v-if="(item % 4 == 1 && item<=topYear*4+1)"
                      @click="selectItem(item,'A')"
                      class="py-5"
                      :color="uLarge && item == isMouseOverItem? 'blue darken-4':(isSelected(item,'A')==1?'green':(item == isMouseOverItem? 'blue': 'grey lighten-1'))"
                      ref="upIcon"
                      @mouseover="uLarge = true"
                      @mouseleave="uLarge = false"
                      :disabled="!(isSelected(item,'A')!= 0)"
                      :small="item == isMouseOverItem && uLarge ? false : true"
                    >{{ isSelected(item,'A')!= 0?'mdi-arrow-up-bold':'t'}}</v-icon>
                    <v-icon
                      v-if="(item % 4 == 1 && item<=topYear*4+1)"
                      @click="selectItem(item,'AB')"
                      ref="eqIcon"
                      class="py-5"
                      :color="eLarge && item == isMouseOverItem ? 'blue darken-4' : (isSelected(item,'AB')==1?'green':(item == isMouseOverItem? 'blue' : 'grey lighten-1'))"
                      :disabled="!(isSelected(item,'AB')!= 0)"
                      @mouseover="eLarge = true"
                      @mouseleave="eLarge = false"
                      :small="item == isMouseOverItem && eLarge ? false : true"
                    >{{ isSelected(item,'AB')!= 0?'mdi-view-stream':'t'}}</v-icon>
                    <v-icon
                      v-if="(item % 4 == 1 && item<=topYear*4+1)"
                      @click="selectItem(item,'B')"
                      class="py-5"
                      ref="dwIcon"
                      :color="dLarge && item == isMouseOverItem? 'blue darken-4':(isSelected(item,'B')==1?'green':(item == isMouseOverItem? 'blue': 'grey lighten-1'))"
                      :disabled="!(isSelected(item,'B')!= 0)"
                      @mouseover="dLarge = true"
                      @mouseleave="dLarge = false"
                      :small="item == isMouseOverItem && dLarge ? false : true"
                    >{{ isSelected(item,'B') != 0 ?'mdi-arrow-down-bold':'t'}}</v-icon>
                  </td>
                </tr>
              </table>
            </v-row>
          </v-col>
        </v-row>

        <v-row justify="center" align="center">
          <v-col cols="2">
            <v-row justify="center" align="center">
              <span
                class="font-weight-bold"
                :class="dLarge?'headline blue--text text--darken-4':'title'"
              >偏好B</span>
            </v-row>
          </v-col>
          <v-col cols="10">
            <v-row justify="center" align="center">
              <table border="1" cellspacing="0" cellpadding="0" ref="table3">
                <tr style="height: 50px">
                  <td
                    v-for="item in 8 * topYear"
                    :key="item"
                    style="text-align: center; width: 16px"
                    :class="item<topYear*4+1?(parseInt((item - 1) / 4) % 2 == 1 ? 'blue lighten-3' : 'blue darken-1'):(parseInt((item - 1) / 4) % 2 == 1 ? 'green lighten-3' : 'green darken-1')"
                  ></td>
                </tr>
              </table>
            </v-row>
          </v-col>
        </v-row>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="primary" @click="reSelect">
          <v-icon large>refresh</v-icon>
        </v-btn>
        <v-btn color="primary">
          <v-icon large>mdi-arrow-right-circle-outline</v-icon>
        </v-btn>
        <v-spacer></v-spacer>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
export default {
  data: () => ({
    topYear: 10,
    isMouseOverItem: -1,
    uLarge: false,
    eLarge: false,
    dLarge: false,
    itemList: [],
    itemIndex: []
  }),
  methods: {
    selectItem(k, v) {
      if (
        !(
          (this.itemIndex.length == 0 && k == this.topYear * 4 + 1) ||
          (this.itemIndex.length > 0 &&
            k == this.itemIndex[this.itemIndex.length - 1] - 4)
        )
      ) {
        alert("请从右至左依次按顺序回答！");
        return;
      }
      // 当选项已经选择，单击选项不会再次记录答案
      if (this.isSelected(k, v) == -1) {
        this.itemList.push({
          index: k,
          type: v
        });
        this.itemIndex.push(k);
      }
      console.log(this.itemList);
      console.log(this.isSelected(k, v));
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
      this.isMouseOverItem = -1;
      this.uLarge = false;
      this.eLarge = false;
      this.dLarge = false;
      this.itemList = [];
      this.itemIndex = [];
      this.$store.dispatch("setNstpPage", 1);
    }
  },
  computed: {
    // 判断选项是否选择，选项已选择且为当前答案，返回记录1；选项已选择且非当前单击答案，返回0；选择未选择返回-1.
    isSelected: function() {
      return function(item, type) {
        for (var i = 0; i < this.itemList.length; i++) {
          if (this.itemList[i].index == item && this.itemList[i].type != type) {
            return 0;
          }
          if (this.itemList[i].index == item && this.itemList[i].type == type) {
            return 1;
          }
        }
        return -1;
      };
    }
  }
};
</script>
