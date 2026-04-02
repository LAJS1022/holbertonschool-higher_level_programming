document.querySelector('#add_item').addEventListener('click', function () {
  document.querySelector('.my_list').appendChild(document.createElement('li')).textContent = 'Item';
});
