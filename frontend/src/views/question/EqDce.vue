<template>
  <v-container>
    <v-row>
      <v-col>
        <v-alert dense type="info"
          >Which is better, state A or state B?</v-alert
        >
      </v-col>
    </v-row>
    <v-row v-for="item in decQuestion" :key="item.name">
      <v-col cols="12" v-if="item.Block == block && item.Name == name">
        <v-row align="center" justify="center">
          <v-col cols="4">
            <v-card
              style="height:200px"
              class="pa-3"
              checked:false
              v-on:click="greet"
            >
              <h3>{{ item.AnswerA }}</h3>
              <p>{{ item.SourceA }}</p>
            </v-card>
          </v-col>
          <v-col cols="4">
            <v-card style="height:200px" class="pa-3" @click="changeCss(item)">
              <h3>{{ item.AnswerB }}</h3>
              <p>{{ item.SourceB }}</p>
            </v-card>
          </v-col>
        </v-row>
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
import dataDce from "@/assets/data/dce.json";
export default {
  name: "EqDce",
  props: ["block1", "startTime"],
  data: () => ({
    decQuestion: [{}],
    block: 1,
    itemOrder: 0,
    name: dataDce[0].Name
  }),
  created() {
    this.decQuestion = dataDce;
  },
  mounted() {
    console.log(this.decQuestion);
  },
  methods: {
    nextBtn() {
      this.itemOrder++;
      console.log(dataDce[this.itemOrder].Name);
      if (dataDce[this.itemOrder].Name == undefined) {
        alert("ssss");
      } else {
        this.name = dataDce[this.itemOrder].Name;
      }
    },
    changeCss(item) {
      item.selected = true;
    }
  }
};
</script>
