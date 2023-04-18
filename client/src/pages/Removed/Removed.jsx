import React from "react";

import MovedFiles from "../../components/MovedFiles/MovedFiles"

function Removed() {
  return (
    <div>
      <MovedFiles
        url={'files/basket'}
        title={'Здесь хранятся ваши удалённые файлы'}
        titleIcon={<img src="img/categories/delete.png" alt="removed" />}
        labelTitle={'удаленным файлам'}
        background='rgb(243 217 220 / 60%)'
        contextMenuBack='Убрать из корзины'
        isFavorite={false}
      />
    </div>
  );
};

export default Removed;
