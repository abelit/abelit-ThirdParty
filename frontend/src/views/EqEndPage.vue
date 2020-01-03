<template>
  <v-container>
    <v-row align="center" justify="center">
      <v-col>
        <v-card height="800">
          <v-card-title class="display-1">Thank You!</v-card-title>
          <v-card-text class="display-1 text-center mt-12" style="padding-top: 200px;">
            <v-row align="center" justify="center">
              <v-col
                cols="4"
                class="light-green lighten-1 py-auto"
                style="height: 200px; padding-top: 60px"
                @click="saveAnswer"
              >
                <span>调查结束</span>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapState } from 'vuex';
export default {
  methods: {
    saveAnswer() {
      console.log(this.allAnswer);
      var url = "";
      if (this.allAnswer[0].questionid == 1) {
        url = "/api/answer/dce/addall"
      } else if (this.allAnswer[0].questionid == 2) {
        url = "/api/answer/tto/addall"
      } else if (this.allAnswer[0].questionid == 3) {
        url = "/api/answer/ttofeedback/addall"
      } else if (this.allAnswer[0].questionid == 4){
        url = "/api/answer/open/addall"
      } else {
        alert("后台地址不对")
      }
      this.$axios.post(url, this.allAnswer);
    }
  },
  computed: {
    ...mapState(["allAnswer"])
  }
}
</script>