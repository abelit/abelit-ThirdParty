<template>
  <div>
    <div v-for="item in eqTtoQuestions" :key="item.id">
    <nstp-tto-a v-if="nstpPage == 1 && eqTtoQuestions.indexOf(item)===currentItem" :block="item"  v-on:cUpdateItem="pUpdateItem($event)"></nstp-tto-a>
    <nstp-tto-b v-if="nstpPage == 2 && eqTtoQuestions.indexOf(item)===currentItem" :block="item" v-on:cUpdateItem="pUpdateItem($event)"></nstp-tto-b>
        </div>
      <v-row>
      <v-dialog v-model="popupDialog" persistent max-width="600">
        <v-card class="pt-5 yellow lighten-4">
          <v-card-text
            class="display-1"
          >{{ eqLangLabels[$vuetify.lang.current].popup_window_exmple }}</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="light-green darken-3"
              @click="popupDialog = false"
              large
            >{{ eqLangLabels[$vuetify.lang.current].btn_ok_exmple }}</v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
  </div>
  
</template>


<script>
import NstpTtoA from "@/views/question/NstpTtoA";
import NstpTtoB from "@/views/question/NstpTtoB";
import { mapState } from "vuex";

export default {
  data: () => ({
    eqTtoQuestions: [{}],
    popupDialog: true,
    currentItem: 0,
    nstpttoAnswers: []
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
      this.nstpttoAnswers.push(data);
      // console.log(this.nstpttoAnswers);
      this.currentItem++;
      // console.log(this.currentItem);
      // console.log(this.eqTtoQuestions.length)
      if (this.currentItem > this.eqTtoQuestions.length - 1) {
        this.$store.dispatch("setAllAnswer", this.nstpttoAnswers);
        this.$router.push({ path: "/eq/end" });
      }
    },
    getQuestion() {
      // console.log(this.userInfo.blockQuestion);
      this.$axios
        .get("/api/question/nstptto", {
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
  },
  created() {
    this.getQuestion();
  }
};
</script>