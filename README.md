# abelit-ThirdParty

```dotnetcli
update `dce_question` set block=replace(block,'.0','') where block like '%.0';
update `tto_question` set block=replace(block,'.0','') where block like '%.0';
update `newtto_question` set block=replace(block,'.0','') where block like '%.0';
update `nstptto_question` set block=replace(block,'.0','') where block like '%.0';
update `ttofeedback_question` set block=replace(block,'.0','') where block like '%.0';
update `opened_question` set block=replace(block,'.0','') where block like '%.0';
```