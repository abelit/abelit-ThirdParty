<template>
  <v-container>
    <v-tabs background-color="#036f90" center-active dark>
      <v-tab @click="type = 1" class="title">{{$vuetify.lang.t('$vuetify.tab.uploadQuestion')}}</v-tab>
      <v-tab @click="type = 2" class="title">{{$vuetify.lang.t('$vuetify.tab.manualInput')}}</v-tab>
      <v-tab
        @click="type = 0; tablePHeaders=[]; tablePData=[]"
        class="title"
      >{{$vuetify.lang.t('$vuetify.tab.interviewer')}}</v-tab>
      <v-tab
        @click="type = 3; tableHeaders=[]; tableData=[]; qtype=''"
        class="title"
      >{{$vuetify.lang.t('$vuetify.tab.question')}}</v-tab>
      <v-tab
        @click="type = 4; tablePHeaders=[]; tablePData=[]; qtype=''"
        class="title"
      >{{$vuetify.lang.t('$vuetify.tab.answer')}}</v-tab>
      <v-tab @click="type = 5" class="title">{{$vuetify.lang.t('$vuetify.tab.versionSetting')}}</v-tab>
      <v-tab @click="type = 6" class="title">{{$vuetify.lang.t('$vuetify.tab.dataInit')}}</v-tab>
    </v-tabs>
    <div v-if="type==1" style="margin-top: 15%">
      <v-row justify="center">
        <v-col cols="12">
          <v-row class="px-10">
            <v-subheader>{{$vuetify.lang.t('$vuetify.tab.uploadQuestion')}}</v-subheader>
            <v-file-input
              v-model="file"
              :label="$vuetify.lang.t('$vuetify.tab.selectFile')"
              :show-size="1000"
              outlined
              dense
            ></v-file-input>
            <v-btn
              color="#036f90"
              dark
              @click="uploadFile"
              class="ml-3"
            >{{$vuetify.lang.t('$vuetify.tab.upload')}}</v-btn>
            <v-btn
              color="#036f90"
              dark
              @click="downloadExampleFile"
              class="ml-3"
            >{{$vuetify.lang.t('$vuetify.tab.downloadExampleQuestion')}}</v-btn>
          </v-row>
        </v-col>
      </v-row>
    </div>
    <div v-if="type==2" style="margin-top: 15%">
      <span>此模块尚未开放</span>
    </div>

    <div v-if="type==3">
      <v-row class="mx-1">
        <v-col cols="12">
          <v-row>
            <!-- <v-subheader>{{$vuetify.lang.t('$vuetify.tab.questionType')}}</v-subheader> -->
            <v-select
              :items="questionTypes"
              v-model="qtype"
              item-value="id"
              item-text="name"
              :label="$vuetify.lang.t('$vuetify.tab.selectQuestionType')"
              outlined
              dense
              @change="getQuestionVersion"
            ></v-select>

            <!-- <v-subheader>{{$vuetify.lang.t('$vuetify.tab.version')}}</v-subheader> -->
            <v-select
              :items="questionVersions"
              v-model="qversion"
              item-value="version"
              item-text="version"
              :label="$vuetify.lang.t('$vuetify.tab.selectVersion')"
              outlined
              dense
            ></v-select>
            <v-btn
              color="#036f90"
              dark
              @click="getQuestion"
              class="ml-3"
            >{{$vuetify.lang.t('$vuetify.tab.query')}}</v-btn>
            <v-btn
              color="error"
              dark
              @click="deleteDialog = true"
              class="ml-3"
            >{{$vuetify.lang.t('$vuetify.tab.deleteQuestion')}}</v-btn>
            <v-dialog v-model="deleteDialog" max-width="500">
              <v-card justify="center" align="center">
                <v-card-text class="pt-8 title">你确定删除吗</v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="green darken-1"
                    text
                    @click="deleteDialog = false"
                  >{{$vuetify.lang.t('$vuetify.button.cancel')}}</v-btn>
                  <v-btn
                    color="green darken-1"
                    text
                    @click="deleteQuestion"
                  >{{$vuetify.lang.t('$vuetify.button.confirm')}}</v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-row>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12">
          <v-data-table
            :headers="tableHeaders"
            :items="tableData"
            :items-per-page="10"
            class="elevation-1"
          ></v-data-table>
        </v-col>
      </v-row>
    </div>

    <div v-if="type==4">
      <v-row class="mx-1">
        <v-col cols="12">
          <v-row>
            <v-select
              :items="answerVersions"
              v-model="aversion"
              item-value="version"
              item-text="version"
              :label="$vuetify.lang.t('$vuetify.tab.selectVersion')"
              outlined
              dense
            ></v-select>
            <v-btn
              class="ml-3"
              color="#036f90"
              dark
              @click="getParticipant"
            >{{$vuetify.lang.t('$vuetify.tab.query')}}</v-btn>
            <v-spacer></v-spacer>
            <v-btn class="ml-3" color="#036f90" dark @click="downloadAnswer('all',1)">
              DCE
              <v-icon small dark>file_download</v-icon>
            </v-btn>
            <v-btn class="ml-3" color="#036f90" dark @click="downloadAnswer('all',2)">
              TTO
              <v-icon small dark>file_download</v-icon>
            </v-btn>
            <v-btn class="ml-3" color="#036f90" dark @click="downloadAnswer('all',3)">
              TTOFeedback
              <v-icon small dark>file_download</v-icon>
            </v-btn>
            <v-btn class="ml-3" color="#036f90" dark @click="downloadAnswer('all',4)">
              Background Questions
              <v-icon small dark>file_download</v-icon>
            </v-btn>
            <v-btn class="ml-3" color="#036f90" dark @click="downloadAnswer('all',5)">
              Non-Stopping TTO
              <v-icon small dark>file_download</v-icon>
            </v-btn>
            <v-btn class="ml-3" color="#036f90" dark @click="downloadAnswer('all',6)">
             Open TTO
              <v-icon small dark>file_download</v-icon>
            </v-btn>
          </v-row>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12">
          <v-data-table
            :headers="tablePHeaders"
            :items="tablePData"
            :items-per-page="10"
            class="elevation-1"
          >
            <template v-slot:item.TTO="{ item }">
              <v-icon
                small
                class="mr-2"
                color="#036f90"
                v-if="item.TTO > 0"
                @click="viewDetailAnswer(item.participant,item.TTO)"
              >remove_red_eye</v-icon>
              <v-icon
                small
                v-if="item.TTO > 0"
                color="primary"
                @click="downloadAnswer(item.participant,item.TTO)"
              >file_download</v-icon>
            </template>
            <template v-slot:item.DCE="{ item }">
              <v-icon
                small
                class="mr-2"
                color="#036f90"
                v-if="item.DCE > 0"
                @click="viewDetailAnswer(item.participant,item.DCE)"
              >remove_red_eye</v-icon>
              <v-icon
                small
                v-if="item.DCE > 0"
                color="primary"
                @click="downloadAnswer(item.participant,item.DCE)"
              >file_download</v-icon>
            </template>
            <template v-slot:item.TTOFeedback="{ item }">
              <v-icon
                small
                class="mr-2"
                color="#036f90"
                v-if="item.TTOFeedback > 0"
                @click="viewDetailAnswer(item.participant,item.TTOFeedback)"
              >remove_red_eye</v-icon>
              <v-icon
                small
                v-if="item.TTOFeedback > 0"
                color="primary"
                @click="downloadAnswer(item.participant,item.TTOFeedback)"
              >file_download</v-icon>
            </template>
            <template v-slot:item.Background_Questions="{ item }">
              <v-icon
                small
                class="mr-2"
                color="#036f90"
                v-if="item.Background_Questions > 0"
                @click="viewDetailAnswer(item.participant,item.Background_Questions)"
              >remove_red_eye</v-icon>
              <v-icon
                small
                v-if="item.Background_Questions > 0"
                color="primary"
                @click="downloadAnswer(item.participant,item.Background_Questions)"
              >file_download</v-icon>
            </template>
            <template v-slot:item.NonStopping_TTO="{ item }">
              <v-icon
                small
                class="mr-2"
                color="#036f90"
                v-if="item.NonStopping_TTO > 0"
                @click="viewDetailAnswer(item.participant,item.NonStopping_TTO)"
              >remove_red_eye</v-icon>
              <v-icon
                small
                v-if="item.NonStopping_TTO > 0"
                color="primary"
                @click="downloadAnswer(item.participant,item.NonStopping_TTO)"
              >file_download</v-icon>
            </template>
            <template v-slot:item.Open_TTO="{ item }">
              <v-icon
                small
                class="mr-2"
                color="#036f90"
                v-if="item.Open_TTO > 0"
                @click="viewDetailAnswer(item.participant,item.Open_TTO)"
              >remove_red_eye</v-icon>
              <v-icon
                small
                v-if="item.Open_TTO > 0"
                color="primary"
                @click="downloadAnswer(item.participant,item.Open_TTO)"
              >file_download</v-icon>
            </template>
          </v-data-table>
        </v-col>
      </v-row>
      <v-row>
        <v-dialog
          v-model="dialog"
          fullscreen
          hide-overlay
          transition="dialog-bottom-transition"
          scrollable
        >
          <v-card tile>
            <v-toolbar flat dark color="primary">
              <v-btn icon dark @click="dialog = false">
                <v-icon>mdi-close</v-icon>
              </v-btn>
              <v-spacer></v-spacer>
              <v-icon
                icon
                dark
                @click="downloadAnswer(tableAData[0].participant,tableAData[0].questionid)"
              >file_download</v-icon>
              <v-toolbar-title></v-toolbar-title>
            </v-toolbar>
            <v-card-text>
              <v-row>
                <v-col cols="12">
                  <v-data-table
                    :headers="tableAHeaders"
                    :items="tableAData"
                    :items-per-page="10"
                    class="elevation-1"
                  ></v-data-table>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
          <div style="flex: 1 1 auto;"></div>
        </v-dialog>
      </v-row>
    </div>
    <div v-if="type==5">
      <v-row justify="center" align="center" style="height: 500px;">
        <v-col cols="4">为开放此模块</v-col>
      </v-row>
    </div>
    <div v-if="type == 6">
      <v-row justify="center" class="mt-12">
        <v-col cols="12" sm="6">
          <v-text-field
            v-model="adminpwd"
            :label="$vuetify.lang.t('$vuetify.tab.inputAdminPass')"
            type="password"
            prepend-inner-icon="lock"
            outlined
            required
            dense
            solo
            flat
          >
            <template v-slot:append-outer>
              <v-btn height="41" dense color="error" dark @click.stop="initdbDialog = true">
                <span>{{$vuetify.lang.t('$vuetify.tab.init')}}</span>
              </v-btn>
              <v-dialog v-model="initdbDialog" max-width="500">
                <v-card>
                  <v-card-title>你确定初始化数据吗？</v-card-title>

                  <v-card-text>
                    <v-alert type="warning">初始化数据将会删除所有题库和答案数据！</v-alert>
                  </v-card-text>

                  <v-card-actions>
                    <v-spacer></v-spacer>

                    <v-btn
                      color="green darken-1"
                      @click="initdbDialog = false"
                    >{{$vuetify.lang.t('$vuetify.button.cancel')}}</v-btn>

                    <v-btn
                      color="green darken-1"
                      @click="initdb"
                    >{{$vuetify.lang.t('$vuetify.button.confirm')}}</v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </template>
          </v-text-field>
        </v-col>
      </v-row>
    </div>
    <div v-if="type==0">
      <v-row class="ml-1">
        <v-col cols="12" sm="6">
          <v-row>
            <!-- <v-select
              :items="answerVersions"
              v-model="aversion"
              item-value="version"
              item-text="version"
              :label="$vuetify.lang.t('$vuetify.tab.version')"
              outlined
              dense
            ></v-select>-->
            <v-btn
              class="ml-3"
              color="#036f90"
              dark
              @click="getInterviewer"
            >{{$vuetify.lang.t('$vuetify.tab.query')}}</v-btn>
          </v-row>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12">
          <v-data-table
            :headers="tablePHeaders"
            :items="tablePData"
            :items-per-page="10"
            class="elevation-1"
          ></v-data-table>
        </v-col>
      </v-row>
    </div>
    <v-snackbar v-model="snackbar" :color="isSuccess?'primary':'#EF5350'" :timeout="3000">{{msg}}</v-snackbar>
  </v-container>
</template>

<script>
import questiontype from "@/assets/data/questiontype.json";
import { mapState } from "vuex";
import XLSX from "xlsx";

export default {
  data: () => ({
    adminpwd: "",
    type: 1,
    file: [],
    msg: "",
    snackbar: false,
    isSuccess: false,
    questionTypes: questiontype,
    questionVersions: [],
    qtype: "",
    qversion: "",
    answerVersions: [
      { version: "V17" },
      { version: "V18" },
      { version: "V19" }
    ],
    aversion: "",
    tableHeaders: [],
    tableData: [],
    dialog: false,
    initdbDialog: false,
    deleteDialog: false,
    tableAHeaders: [],
    tableAData: [],
    tablePHeaders: [],
    tablePData: []
  }),
  methods: {
    uploadFile() {
      let forData = new FormData();
      forData.append("file", this.file);

      if (this.file == "") {
        alert("请选择上传文件！");
      }

      this.$axios
        .post("/api/upload", forData, {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        })
        .then(res => {
          console.log(res);
          this.msg = "文件上传成功！";
          this.snackbar = true;

          //   setTimeout(() => {
          //       this.snackbar = false;
          //   }, 2000);
        })
        .catch(err => {
          console.log(err);
          console.log("failed");
        });
    },
    getQuestion() {
      this.tableHeaders = [];
      this.tableData = [];
      var url;
      switch (this.qtype) {
        case 1:
          url = "/api/question/dce";
          break;
        case 2:
          url = "/api/question/tto";
          break;
        case 3:
          url = "/api/question/ttofeedback";
          break;
        case 4:
          url = "/api/question/open";
          break;
        case 5:
          url = "/api/question/nstptto";
          break;
        case 6:
          url = "/api/question/newtto";
          break;
        default:
          alert("请选择题库类型");
      }
      console.log(this.qversion);
      this.$axios
        .get(url, {
          params: { block: "all", version: this.qversion || "all" }
        })
        .then(res => {
          //   console.log(res.data)
          var objData = res.data;

          var objHeader = [];
          var objKey = Object.keys(objData[0]);

          for (let i = 0; i < objKey.length; i++) {
            objHeader.push({
              text: objKey[i],
              value: objKey[i]
            });
          }

          this.tableHeaders = objHeader;
          this.tableData = objData;
        })
        .catch(err => {
          console.log(err);
        });
    },
    async getAnswer(type, version, participant) {
      this.tableAData = [];
      this.tableAHeaders = [];
      var url;
      console.log(type);
      switch (type) {
        case 1:
          url = "/api/answer/dce";
          break;
        case 2:
          url = "/api/answer/tto";
          break;
        case 3:
          url = "/api/answer/ttofeedback";
          break;
        case 4:
          url = "/api/answer/open";
          break;
        case 5:
          url = "/api/answer/nstptto";
          break;
        case 6:
          url = "/api/answer/newtto";
          break;
        default:
          alert("请选择题库类型！");
      }

      await this.$axios
        .get(url, {
          params: { version: version, participant: participant }
        })
        .then(res => {
          //   console.log(res.data)
          var objData = res.data;

          var objHeader = [];
          var objKey = Object.keys(objData[0]);

          for (let i = 0; i < objKey.length; i++) {
            objHeader.push({
              text: objKey[i],
              value: objKey[i]
            });
          }
          //   console.log(objHeader)
          this.tableAHeaders = objHeader;
          this.tableAData = objData;
          console.log("I am getAnswer function.");
        })
        .catch(err => {
          this.tableAData = [];
          this.tableAHeaders = [];
          console.log(err);
        });
      // console.log(this.qtype);
    },
    getQuestionVersion() {
      this.questionVersions = [];
      var url;
      switch (this.qtype) {
        case 1:
          url = "/api/question/dce";
          break;
        case 2:
          url = "/api/question/tto";
          break;
        case 3:
          url = "/api/question/ttofeedback";
          break;
        case 4:
          url = "/api/question/open";
          break;
        case 5:
          url = "/api/question/nstptto";
          break;
        case 6:
          url = "/api/question/newtto";
          break;
        default:
          alert("题型不存在");
      }

      this.$axios
        .get(url, {
          params: { block: "all" }
        })
        .then(res => {
          var objData = res.data;

          var objVersion = [];

          for (let i = 0; i < objData.length; i++) {
            if (objVersion.indexOf(objData[i].version) == -1) {
              objVersion.push({ version: objData[i].version });
            }
          }
          objVersion.push("all");
          this.questionVersions = objVersion;
        })
        .catch(err => {
          console.log(err);
        });
    },
    getParticipant() {
      this.tablePHeaders = [];
      this.tablePData = [];
      let url = "/api/participant";
      this.$axios
        .get(url, {
          params: { version: this.aversion }
        })
        .then(res => {
          console.log(res.data);
          var objData = res.data;

          var objHeader = [];
          var objKey = Object.keys(objData[0]);

          for (let i = 0; i < objKey.length; i++) {
            objHeader.push({
              text: objKey[i],
              value: objKey[i]
            });
          }
          console.log(objHeader);
          console.log(objData);
          this.tablePHeaders = objHeader;
          this.tablePData = objData;
        })
        .catch(err => {
          console.log(err);
        });
    },
    getInterviewer() {
      this.tablePHeaders = [];
      this.tablePData = [];
      let url = "/api/interviewer";
      this.$axios
        .get(url)
        .then(res => {
          console.log(res.data);
          var objData = res.data;

          var objHeader = [];
          var objKey = Object.keys(objData[0]);

          for (let i = 0; i < objKey.length; i++) {
            objHeader.push({
              text: objKey[i],
              value: objKey[i]
            });
          }
          //   console.log(objHeader)
          this.tablePHeaders = objHeader;
          this.tablePData = objData;
        })
        .catch(err => {
          console.log(err);
        });
    },
    async downloadAnswer(pid, qid) {
      if (this.aversion == "") {
        alert("请选择版本号！");
        return false;
      }

      await this.getAnswer(qid, this.aversion, pid);

      console.log("I am downloadAnswer");
      var filename;
      var questionName;
      var answerTime;

      switch (qid) {
        case 1:
          questionName = "DCE";
          break;
        case 2:
          questionName = "TTO";
          break;
        case 3:
          questionName = "TTO Feedback";
          break;
        case 4:
          questionName = "Background Questions";
          break;
        case 5:
          questionName = "Non-Stopping TTO";
          break;
        case 6:
          questionName = "Open TTO";
          break;
        default:
          questionName = "unkonwn";
      }

      if (this.tableAData.length < 1) {
        alert(questionName + "题型还没有人答题！");
        return;
      }
      answerTime = this.tableAData[0].created_timestamp;

      let syear = new Date(answerTime).getFullYear();
      let smonth = new Date(answerTime).getMonth();
      let sdate = new Date(answerTime).getDate();
      let shour = new Date(answerTime).getHours();

      smonth = smonth + 1;
      if (smonth < 10) {
        smonth = "0" + smonth.toString();
      }

      if (sdate < 10) {
        sdate = "0" + sdate.toString();
      }

      if (shour < 10) {
        shour = "0" + shour.toString();
      }

      if (pid) {
        filename =
          questionName +
          "_" +
          this.aversion +
          "_" +
          pid +
          "_" +
          syear.toString() +
          smonth.toString() +
          sdate.toString() +
          shour.toString();
      } else {
        filename =
          questionName +
          "_" +
          this.aversion +
          "_" +
          syear.toString() +
          smonth.toString() +
          sdate.toString();
      }
      console.log(filename);

      var exportData = XLSX.utils.json_to_sheet(this.tableAData);
      var wb = XLSX.utils.book_new();
      XLSX.utils.book_append_sheet(wb, exportData, questionName + " Answer");
      XLSX.writeFile(wb, filename + ".xlsx");
    },
    viewDetailAnswer(pid, qid) {
      if (this.aversion == "") {
        alert("请选择版本号！");
        return false;
      }

      this.dialog = true;
      console.log({ participant: pid, questionid: qid });
      this.getAnswer(qid, this.aversion, pid);
    },
    initdb() {
      let url = "/admin/initdb";

      this.$axios
        .post(url, {
          adminpwd: this.adminpwd
        })
        .then(res => {
          // console.log(res.data);
          this.isSuccess = true;
          this.msg = "数据初始化成功！";
          this.snackbar = true;
          this.initdbDialog = false;
          this.adminpwd = "";
        })
        .catch(err => {
          this.isSuccess = false;
          if (err.response) {
            this.msg = "管理员密码不正确！";
          } else {
            this.msg = "内部错误！";
          }

          this.snackbar = true;
          this.initdbDialog = false;
          this.adminpwd = "";
        });
    },
    deleteQuestion() {
      let url = "/api/question/delete";
      if (this.qversion == "") {
        this.isSuccess = false;
        this.msg = "未选择题库及对应的版本号！";
        this.snackbar = true;
        return false;
      }
      if (this.qtype == "") {
        this.isSuccess = false;
        this.msg = "未选择题库及对应的版本号！";
        this.snackbar = true;
        return false;
      }

      this.$axios
        .post(url, {
          questionid: this.qtype,
          version: this.qversion
        })
        .then(res => {
          console.log(res.data);
          this.isSuccess = true;
          this.msg = "删除成功！";
          this.snackbar = true;
        })
        .catch(err => {
          console.log(err);
          this.isSuccess = false;
          this.msg = "删除失败";
          this.snackbar = true;
        });
    },
    getAnswerVersion() {
      this.answerVersions = [];
      let url = "/api/answer/version";
      this.$axios
        .get(url)
        .then(res => {
          this.answerVersions = res.data;
        })
        .catch(err => {
          console.log(err);
        });
    },
    downloadExampleFile() {
      let url = "/download/questions.xlsx/";
      this.$axios
        .get(url, { responseType: "blob" })
        .then(res => {
          console.log(res.headers["Content-Disposition"]);
          const url = window.URL.createObjectURL(new Blob([res.data]));
          const link = document.createElement("a");
          link.href = url;

          link.setAttribute("download", "questions.xlsx");
          document.body.appendChild(link);
          link.click();
        })
        .catch(err => {
          console.log(err);
        });
    }
  },
  computed: {
    ...mapState(["qVersion"])
  },
  mounted() {
    // this.getParticipant();
    this.getAnswerVersion();
  }
};
</script>

<style lang="scss">
.v-input__append-outer {
  margin: 0 !important;
}
</style>