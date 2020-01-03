<template>
  <div>
    <template v-for="item in eqTtoQuestions">
      <eq-tto
        v-if="eqTtoQuestions.indexOf(item)===currentItem"
        :block="item"
        :startTime="startTime"
        v-on:cUpdateItem="pUpdateItem($event)"
        :key="item.id"
      ></eq-tto>
    </template>
  </div>
</template>

<script>
import EqTto from "@/views/question/EqTto";
// import dataEqttoquestion from "@/assets/data/eqttoquestion.json";
import { mapState } from "vuex";

export default {
  components: {
    EqTto
  },
  data: () => ({
    eqTtoQuestions: [{}],
    currentItem: 0,
    startTime: 0,
    ttoAnswers: []
  }),
  created() {
    this.getQuestion();
    this.startTime = new Date();
  },
  mounted() {
    console.log("EQ tto Exam")
  },
  computed: {
    ...mapState(["userInfo"])
  },
  methods: {
    pUpdateItem(data) {
      // console.log(this.currentItem + "--->" + this.eqTtoQuestions[this.currentItem].source_text)
      this.ttoAnswers.push(data);
      console.log(this.ttoAnswers)
      this.currentItem++;
      // console.log(this.currentItem);
      // console.log(this.eqTtoQuestions.length)
      if (this.currentItem > this.eqTtoQuestions.length - 1) {
        this.$store.dispatch("setAllAnswer", this.ttoAnswers);
        this.$router.push({ path: "/eq/end" });
      }
    },
    getQuestion() {
      // console.log(this.userInfo.blockQuestion);
      this.$axios
        .get("/api/question/tto", {
          params: { block: this.userInfo.blockQuestion }
        })
        .then(res => {
          this.eqTtoQuestions = res.data;
          // this.currentItem = this.eqTtoQuestions[0].id;
          // console.log(this.eqTtoQuestions);
        })
        .catch(error => {
          console.log(error);
        });
      // console.log(this.eqTtoQuestions);
    }
  }
};
</script>