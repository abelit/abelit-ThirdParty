<template>
  <div class="grey lighten-5" style="width:1440px; margin:auto">
    <v-card justify="center" align="start">
      <v-card-title v-show="true">
        <v-row>
          <v-col>
            <v-alert dense type="info"
              >哪一个选择比较好，生命A、生命B，还是它们大致相同？</v-alert
            >
          </v-col>
        </v-row>
      </v-card-title>
      <v-card-text>
        <v-row justify="center" align="center">
          <v-col cols="2">
            <v-row justify="center" align="center" class="font-weight-bold">
              偏好A
            </v-row>
          </v-col>
          <v-col cols="10">
            <v-row justify="center" align="center">
              <table border="1" cellspacing="0" cellpadding="0" ref="table1">
                <tr style="height: 50px">
                  <td
                    v-for="item in 4 * topYear"
                    :key="item"
                    style="text-align: center; width: 24px"
                    :class="
                      parseInt((item - 1) / 4) % 2 == 1
                        ? 'green lighten-3'
                        : 'green darken-1'
                    "
                  ></td>
                </tr>
              </table>
            </v-row>
          </v-col>
        </v-row>

        <v-row justify="center" align="center">
          <v-col cols="2">
            <v-row justify="center" align="center" class="font-weight-bold">
              A和B大致相同
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
                    @mouseover="mouseOver(item)"
                    @mouseleave="mouseLeave(item)"
                  >
                    <v-icon
                      v-if="item % 4 == 1"
                      @click="printInfo(item + ' up')"
                      class="py-5"
                      :color="
                        uLarge && item == isMouseOverItem
                          ? 'blue darken-4'
                          : item == isMouseOverItem
                          ? 'blue'
                          : 'grey lighten-1'
                      "
                      ref="upIcon"
                      @mouseover="uLarge = true"
                      @mouseleave="uLarge = false"
                      :large="item == isMouseOverItem && uLarge ? true : false"
                      >mdi-arrow-up-bold</v-icon
                    >
                    <v-icon
                      v-if="item % 4 == 1"
                      @click="printInfo(item + ' equal')"
                      ref="eqIcon"
                      class="py-5"
                      :color="
                        eLarge && item == isMouseOverItem
                          ? 'blue darken-4'
                          : item == isMouseOverItem
                          ? 'blue'
                          : 'grey lighten-1'
                      "
                      @mouseover="eLarge = true"
                      @mouseleave="eLarge = false"
                      :large="item == isMouseOverItem && eLarge ? true : false"
                      >mdi-view-stream</v-icon
                    >
                    <v-icon
                      v-if="item % 4 == 1"
                      @click="printInfo(item + 'down')"
                      class="py-5"
                      ref="dwIcon"
                      :color="
                        dLarge && item == isMouseOverItem
                          ? 'blue darken-4'
                          : item == isMouseOverItem
                          ? 'blue'
                          : 'grey lighten-1'
                      "
                      @mouseover="dLarge = true"
                      @mouseleave="dLarge = false"
                      :large="item == isMouseOverItem && dLarge ? true : false"
                      >mdi-arrow-down-bold</v-icon
                    >
                  </td>
                </tr>
              </table>
            </v-row>
          </v-col>
        </v-row>

        <v-row justify="center" align="center">
          <v-col cols="2">
            <v-row justify="center" align="center">
              <span class="font-weight-bold headline">偏好B</span>
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
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  data: () => ({
    topYear: 10,
    isMouseOverItem: -1,
    isMouseOverItem: -1,
    uLarge: false,
    eLarge: false,
    dLarge: false
  }),
  methods: {
    printInfo(param) {
      alert(param);
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
    mouseOverIcon(item) {
      this.isMouseOverIcon = item;
    },
    mouseLeave(item) {
      // if (item % 4 == 1) {
      //   // console.log(this.$refs.iconList[item - 1].children.length);
      //   let eLenth = this.$refs.iconList[item - 1].children.length;
      //   for (var i = 0; i < eLenth; i++) {
      //       this.$refs.iconList[item - 1].children[i].style.color = "#BDBDBD";
      //   }
      // }
      this.isMouseOverItem = -1;
      this.isMouseOverIcon = -1;
    }
  }
};
</script>
