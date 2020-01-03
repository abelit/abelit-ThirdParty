<template>
  <v-container>
    <v-tabs background-color="primary" center-active dark>
      <v-tab @click="type = 1">上传题库</v-tab>
      <v-tab @click="type = 2">手动填写</v-tab>
      <v-tab @click="type = 3;tableHeaders=[];tabledata=[];qtype=''">查看题库</v-tab>
      <v-tab @click="type = 4;tableHeaders=[];tabledata=[];qtype=''">查看答案</v-tab>
    </v-tabs>
    <div v-if="type==1" style="margin-top: 15%">
      <v-row>
        <v-col cols="12">
          <v-row class="px-10">
            <v-subheader>上传题库</v-subheader>
            <v-file-input v-model="file" label="选择文件" :show-size="1000" outlined></v-file-input>
          </v-row>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12">
          <v-row justify="end" class="px-10">
            <v-btn color="primary" @click="uploadFile">上传</v-btn>
          </v-row>
        </v-col>
      </v-row>
      <v-snackbar v-model="snackbar" color="primary" :timeout="2000">{{msg}}</v-snackbar>
    </div>
    <div v-if="type==2" style="margin-top: 15%">
      <span>此模块尚未开放</span>
    </div>

    <div v-if="type==3">
      <v-row>
        <v-col cols="3">
          <v-row>
            <v-col>
              <v-subheader>题目类型</v-subheader>
            </v-col>
            <v-col>
              <v-select
                :items="questionTypes"
                v-model="qtype"
                item-value="id"
                item-text="name"
                label="选题题型"
                outlined
                @change="getQuestionVersion"
              ></v-select>
            </v-col>
          </v-row>
        </v-col>
        <v-col cols="3">
          <v-row>
            <v-col>
              <v-subheader>题库版本</v-subheader>
            </v-col>
            <v-col>
              <v-select
                :items="questionVersions"
                v-model="qversion"
                item-value="version"
                item-text="version"
                label="选择版本号"
                outlined
              ></v-select>
            </v-col>
          </v-row>
        </v-col>
        <v-col cols="3" class="pa-8">
          <v-btn color="primary" @click="getQuestion" large>
            <v-icon>search</v-icon>
          </v-btn>
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
      <v-row>
        <v-col cols="6">
          <v-row>
            <v-subheader>题目类型</v-subheader>
            <v-select
              :items="questionTypes"
              v-model="qtype"
              item-value="id"
              item-text="name"
              label="选择题型"
              outlined
              @change="getAnswer"
            ></v-select>
          </v-row>
        </v-col>
        <!-- <v-col>
          <v-btn color="success" @click="getQuestion">getQuestion</v-btn>
        </v-col>-->
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
  </v-container>
</template>

<script>
import questiontype from "@/assets/data/questiontype.json";
export default {
  data: () => ({
    type: 1,
    file: [],
    msg: "",
    snackbar: false,
    questionTypes: questiontype,
    questionVersions: [],
    qtype: "",
    qversion: "",
    tableHeaders: [],
    tableData: []
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
        .catch(error => {
          console.log("failed");
        });
    },
    getQuestion() {
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
        default:
          alert("题型不存在");
      }
      console.log(this.qversion);
      this.$axios
        .get(url, {
          params: { block: "all", version: ""}
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
    getAnswer() {
      var url;
      switch (this.qtype) {
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
        default:
          alert("题型不存在");
      }

      this.$axios
        .get(url)
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
          this.tableHeaders = objHeader;
          this.tableData = objData;
        })
        .catch(err => {
          console.log(err);
        });
      console.log(this.qtype);
    },
    getQuestionVersion() {
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
        default:
          alert("题型不存在");
      }

      this.$axios
        .get(url, {
          params: { block: "all"}
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
    }
  }
};
</script>

