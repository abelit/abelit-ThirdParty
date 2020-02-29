<template>
  <v-container fluid fill-height>
    <!-- <v-row>
      <v-icon color="primary">mdi-arrow-up-bold</v-icon>
      <v-icon color="primary">mdi-arrow-up-bold-outline</v-icon>
      <v-icon color="primary">mdi-arrow-down-bold</v-icon>
      <v-icon color="primary">mdi-arrow-down-bold-outline</v-icon>

      <v-icon color="primary">mdi-equal</v-icon>
      <v-icon color="primary">mdi-equal-box</v-icon>
      <v-icon color="primary">mdi-view-stream</v-icon>
    </v-row>-->
    <v-row class="mx-0">
      <v-row justify="center" align="center">
        <v-col :cols="$vuetify.breakpoint.mdAndDown ? 2 : 2">
          <v-row :justify="$vuetify.breakpoint.mdAndDown ? 'center' : 'end'"
            >偏好A</v-row
          >
        </v-col>
        <v-col :cols="$vuetify.breakpoint.mdAndDown ? 10 : 9">
          <v-row justify="center" no-getters>
            <table
              border="1"
              cellspacing="0"
              cellpadding="0"
              ref="table1"
              style="table-layout: fixed"
            >
              <tr style="height: 50px">
                <td
                  v-for="item in range(topYear)"
                  :key="item"
                  style="text-align: center; width: 24px;"
                  :class="
                    parseInt((item - 1) / 4) % 2 == 1 ? initClass3 : initClass4
                  "
                ></td>
              </tr>
            </table>
          </v-row>
        </v-col>
      </v-row>
      <v-row justify="center" align="center">
        <v-col :cols="$vuetify.breakpoint.mdAndDown ? 2 : 2" style="margin-left: 72px">
          <v-row :justify="$vuetify.breakpoint.mdAndDown ? 'center' : 'end'"
            >A和B基本一样</v-row
          >
        </v-col>
        <v-col :cols="$vuetify.breakpoint.mdAndDown ? 10 : 9">
          <v-row justify="center" align="center">
            <table
              border="0"
              cellspacing="0"
              cellpadding="0"
              ref="table1"
              style="table-layout: fixed"
            >
              <tr style="height: 50px">
                <td
                  v-for="item in range(topYear + 1)"
                  :key="item"
                  style="text-align: center; width: 24px;"
                  @mouseover="initColor1='indigo';large=true"
                  @mouseleave="initColor1='grey'"
                >
                  <v-icon
                    v-if="item % 4 == 1"
                    :color="initColor1"
                    @click="printInfo(item + ' up');initColor1='red'"
                    :large='large'
                    dark
                    disabled
                    class="pt-5"
                    >mdi-arrow-up-bold</v-icon
                  >
                  <v-icon
                    v-if="item % 4 == 1"
                    :color="initColor1"
                    @click="printInfo(item + ' equal')"
                    class="pt-5"
                    >mdi-view-stream</v-icon
                  >
                  <v-icon
                    v-if="item % 4 == 1"
                    :color="initColor1"
                    @click="printInfo(item + 'down')"
                    class="pt-5"
                    >mdi-arrow-down-bold</v-icon
                  >
                </td>
              </tr>
            </table>
          </v-row>
        </v-col>
      </v-row>
      <v-row justify="center" align="center">
        <v-col :cols="$vuetify.breakpoint.mdAndDown ? 2 : 2">
          <v-row :justify="$vuetify.breakpoint.mdAndDown ? 'center' : 'end'"
            >偏好B</v-row
          >
        </v-col>
        <v-col :cols="$vuetify.breakpoint.mdAndDown ? 10 : 9">
          <v-row justify="center">
            <table
              border="1"
              cellspacing="0"
              cellpadding="0"
              ref="table1"
              style="table-layout: fixed"
            >
              <tr style="height: 50px">
                <td
                  v-for="item in range(topYear)"
                  :key="item"
                  style="width: 24px"
                  :class="
                    parseInt((item - 1) / 4) % 2 == 1 ? initClass1 : initClass2
                  "
                ></td>
              </tr>
            </table>
          </v-row>
        </v-col>
      </v-row>
    </v-row>
  </v-container>
</template>

<script>
/** 逻辑： 1、全选A，完成11步回答后进入20年页面，20年回答完不会返回10年页面，总共22次回答；
 * 2、第一次选A，第二次开始不选A，回答完11道题后追加问一道题，比如9年零3个月，9年零6个月；
 * 3、其他情况按步回答完11道题即可。

*/

export default {
  data() {
    return {
      topYear: 10,
      initClass1: "blue lighten-3",
      initClass2: "blue darken-1",
      initClass3: "green lighten-3",
      initClass4: "green darken-1",
      initColor1: 'grey',
      large: false
    };
  },
  computed: {
    range: function() {
      return function(year) {
        var arr = [];
        for (var i = 1; i <= 4 * year; i++) {
          arr.push(i);
        }
        return arr;
      };
    }
  },
  methods: {
    printInfo(param) {
      alert(param);
    }
  }
};
</script>

<style lang="scss">
.app-td {
}
</style>
