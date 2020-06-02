<template>
  <div>
    <template v-for="item in eqTtoQuestions">
      <eq-tto-new
        v-if="eqTtoQuestions.indexOf(item)===currentItem"
        :block="item"
        :startTime="startTime"
        v-on:cUpdateItem="pUpdateItem($event)"
        :key="item.id"
      ></eq-tto-new>
    </template>
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
import EqTtoNew from "@/views/question/EqTtoNew";
import { mapState } from "vuex";

export default {
  components: {
    EqTtoNew
  },
  data: () => ({
    eqTtoQuestions: [{}],
    currentItem: 0,
    startTime: 0,
    newttoAnswers: [],
    popupDialog: true
  }),
  created() {
    this.getQuestion();
    this.startTime = new Date();
  },
  mounted() {
    console.log("EQ tto Exam");
    // console.log(this.eqLangLabels);
  },
  computed: {
    ...mapState(["userInfo", "qVersion", "eqLangLabels"])
  },
  methods: {
    pUpdateItem(data) {
      console.log(this.newttoAnswers);
      this.currentItem++;
      data.position_of_item = this.currentItem;
      this.newttoAnswers.push(data);
      // console.log(this.currentItem);
      // console.log(this.eqTtoQuestions.length)
      if (this.currentItem > this.eqTtoQuestions.length - 1) {
        this.$store.dispatch("setAllAnswer", this.newttoAnswers);
        this.$router.push({ path: "/eq/end" });
      }
    },
    getQuestion() {
      // console.log(this.userInfo.blockQuestion);
      this.$axios
        .get("/api/question/newtto", {
          params: { block: this.userInfo.blockQuestion, version: this.qVersion }
        })
        .then(res => {
          let common_arr = res.data.filter(item => isNaN(item.block));
          let random_arr = res.data.filter(item => !isNaN(item.block)).sort(() => Math.random() - 0.5);
          // let common_arr = res.data.slice(0, 6);
          // let random_arr = res.data.slice(6).sort(() => Math.random() - 0.5);
          // console.log(random_arr)
          // this.eqTtoQuestions = res.data.sort(() => Math.random() - 0.5);
          this.eqTtoQuestions = common_arr.concat(random_arr);
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