<template>
  <div>
    <nstp-tto-a v-if="nstpPage == 1"></nstp-tto-a>
    <nstp-tto-b v-if="nstpPage == 2"></nstp-tto-b>
  </div>
</template>


<script>
import NstpTtoA from "@/views/question/NstpTtoA";
import NstpTtoB from "@/views/question/NstpTtoB";
import { mapState } from "vuex";

export default {
  data: () => ({
    eqTtoQuestions: [{}]
  }),
  components: {
    NstpTtoA,
    NstpTtoB
  },
  computed: {
    ...mapState(["nstpPage", "userInfo", "qVersion", "eqLangLabels"])
  },
  methods: {
    pUpdateItem(data) {
      this.ttoAnswers.push(data);
      // console.log(this.ttoAnswers);
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
          params: { block: this.userInfo.blockQuestion, version: this.qVersion }
        })
        .then(res => {
          this.eqTtoQuestions = res.data.sort(() => Math.random() - 0.5);
          console.log(this.eqTtoQuestions);
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