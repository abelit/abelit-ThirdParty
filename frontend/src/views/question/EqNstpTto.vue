<template>
  <div>
    <div v-for="item in eqTtoQuestions" :key="item.id">
      <nstp-tto-a
        v-if="nstpPage == 1 && eqTtoQuestions.indexOf(item) === currentItem"
        :block="item"
        v-on:cUpdateItem="pUpdateItem($event)"
      ></nstp-tto-a>
      <nstp-tto-b
        v-if="nstpPage == 2 && eqTtoQuestions.indexOf(item) === currentItem"
        :block="item"
        v-on:cUpdateItem="pUpdateItem($event)"
        v-on:cDeleteItem="pDeleteItem($event)"
      ></nstp-tto-b>
    </div>
    <v-row>
      <v-dialog v-model="popupDialog" persistent max-width="600">
        <v-card class="pt-5 yellow lighten-4">
          <v-card-text class="display-1">{{
            eqLangLabels[$vuetify.lang.current].popup_window_exmple
          }}</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="light-green darken-3"
              @click="popupDialog = false"
              large
              >{{ eqLangLabels[$vuetify.lang.current].btn_ok_exmple }}</v-btn
            >
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

var intervalTimer;

export default {
  data: () => ({
    eqTtoQuestions: [{}],
    popupDialog: true,
    currentItem: 0,
    nstpttoAnswers: [],
    disTime: 0,
    disFormatTime: "00:00:00",
    reset: 0
  }),
  components: {
    NstpTtoA,
    NstpTtoB,
  },
  computed: {
    ...mapState(["nstpPage", "userInfo", "qVersion", "eqLangLabels"]),
  },
  methods: {
    countTime() {
      intervalTimer = setInterval(() => {
        this.disTime = this.disTime + 1;
        this.disFormatTime = this.displayTime(this.disTime);
      }, 1000);
    },
    displayTime(time) {
      const hours = Math.floor(time / 3600);
      const minutes = Math.floor(time / 60);
      const seconds = time % 60;

      return `${this.zeroPadded(hours)}:${this.zeroPadded(
        minutes
      )}:${this.zeroPadded(seconds)}`;
    },
    zeroPadded(num) {
      // 4 --> 04
      return num < 10 ? `0${num}` : num;
    },
    pDeleteItem(data) {
      this.nstpttoAnswers = this.nstpttoAnswers.filter(item => item.item != data.item);
      this.reset++;
      // console.log(this.nstpttoAnswers);
      console.log(data.item)
    },
    pUpdateItem(data) {
      data.arr.map((item) => (item.used_time = this.disTime));
      data.arr.map((item) => (item.position_of_item = this.currentItem + 1));
      this.nstpttoAnswers = this.nstpttoAnswers.concat(data.arr);
      console.log(this.nstpttoAnswers);
      if (data.next) {
        this.currentItem++;
        // console.log(this.currentItem);
        // console.log(this.eqTtoQuestions.length)
        this.$store.dispatch("setNstpPage", 1);
        if (this.currentItem > this.eqTtoQuestions.length - 1) {
          var result = [];

          this.nstpttoAnswers.forEach(
            ((hash) => (a) => {
              if (!hash[a.position_of_item]) {
                hash[a.position_of_item] = {
                  position_of_item: a.position_of_item,
                  used_time: 0,
                };
                result.push(hash[a.position_of_item]);
              }
              hash[a.position_of_item].used_time = Math.max(
                hash[a.position_of_item].used_time,
                a.used_time
              );
            })(Object.create(null))
          );

          this.nstpttoAnswers.map(function(i) {
            //console.log(i.position_of_item)
            result.map(function(j) {
              if (i.position_of_item == j.position_of_item) {
                i.used_time = j.used_time;
              }
            });
          });

          console.log(this.nstpttoAnswers)

          this.$store.dispatch("setAllAnswer", this.nstpttoAnswers);
          this.$router.push({ path: "/eq/end" });
        }
        this.nstpttoAnswers.map(item => item.reset += this.reset);
        console.log(this.nstpttoAnswers)
        console.log(this.disFormatTime);

        // clearInterval(intervalTimer);
        this.disTime = 0;
      }
    },
    getQuestion() {
      // console.log(this.userInfo.blockQuestion);
      this.$axios
        .get("/api/question/nstptto", {
          params: {
            block: this.userInfo.blockQuestion,
            version: this.qVersion,
          },
        })
        .then((res) => {
          let common_arr = res.data.slice(0, 6);
          let random_arr = res.data.slice(6).sort(() => Math.random() - 0.5);
          this.eqTtoQuestions = common_arr.concat(random_arr);
          // this.eqTtoQuestions = res.data.sort(() => Math.random() - 0.5);
          // console.log(this.eqTtoQuestions);
          // this.currentItem = this.eqTtoQuestions[0].id;
          // console.log(this.eqTtoQuestions);
        })
        .catch((error) => {
          console.log(error);
        });
      // console.log(this.eqTtoQuestions);
    },
  },
  created() {
    this.getQuestion();
  },
  mounted() {
    this.countTime();
  },
};
</script>
