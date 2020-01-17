<template>
  <v-container>
    <v-row>
      <v-col>
        <v-card min-height="800" max-height="1080" justify="center" align="center">
          <v-card-title class="display-1 pa-12">{{ eqLangLabels[$vuetify.lang.current].T10 }}</v-card-title>
          <v-card-text
            class="display-1 pa-12 light-green lighten-2"
            style="margin-top: 100px;width: 500px;"
            disabled
            @click="saveAnswer"
          >
            <!-- {{ eqLangLabels[$vuetify.lang.current].T11 }} -->
            <v-progress-circular
              :size="200"
              :width="isCircle?7:0"
              :color="isCircle?'primary':''"
              :indeterminate="isCircle"
            >
              <span color="success">{{ eqLangLabels[$vuetify.lang.current].T11 }}</span>
            </v-progress-circular>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-snackbar v-model="snackbar">数据已经成功入库！</v-snackbar>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapState } from "vuex";
export default {
  data: () => ({
    isCircle: false,
    isSave: false,
    snackbar: false
  }),
  methods: {
    saveAnswer() {
      // console.log(this.allAnswer);
      if (this.isSave) {
        alert("数据已经提交入库！");
        return false;
      }
      var url = "";
      if (this.allAnswer[0].questionid == 1) {
        url = "/api/answer/dce/addall";
      } else if (this.allAnswer[0].questionid == 2) {
        url = "/api/answer/tto/addall";
      } else if (this.allAnswer[0].questionid == 3) {
        url = "/api/answer/ttofeedback/addall";
      } else if (this.allAnswer[0].questionid == 4) {
        url = "/api/answer/open/addall";
      } else {
        alert("后台地址不对");
      }
      this.$axios
        .post(url, this.allAnswer)
        .then(res => {
          if (res.status == 200) {
            this.isCircle = true;
            this.snackbar = true;
            setTimeout(() => {
              this.isCircle = false;
              this.snackbar = false;
              this.$router.push({ path: "/" });
            }, 5000);
          }
          this.isSave = true;
        })
        .catch(err => {
          console.log(err);
        });
    }
  },
  computed: {
    ...mapState(["allAnswer", "eqLangLabels"])
  }
};
</script>