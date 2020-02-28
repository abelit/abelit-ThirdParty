<template>
  <v-container>
    <v-row>
      <v-icon color="primary">mdi-arrow-up-bold</v-icon>
      <v-icon color="primary">mdi-arrow-up-bold-outline</v-icon>
      <v-icon color="primary">mdi-arrow-down-bold</v-icon>
      <v-icon color="primary">mdi-arrow-down-bold-outline</v-icon>

      <v-icon color="primary">mdi-equal</v-icon>
      <v-icon color="primary">mdi-equal-box</v-icon>
      <v-icon color="primary">mdi-view-stream</v-icon>
      <table border="1" cellspacing="0" cellpadding="0" ref="table1">
        <tr style="height: 50px">
          <td
            v-for="item in range(topYear)"
            :key="item"
            style="text-align: center; width: 24px"
            :class="(item+1) % 5 == 1 ? 'light-green lighten-1' : 'light-green darken-2'"
          ></td>
        </tr>
      </table>
      {{range(topYear)}}
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
            topYear: 10
        }
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
    },
  }
}
</script>
