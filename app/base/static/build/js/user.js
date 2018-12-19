function modify_user_form() { // eslint-disable-line no-unused-vars
  if ($('#modify_user_form').parsley().validate()) {
    $.ajax({
      type: 'POST',
      url: '/management/users/modify_user',
      dataType: 'json',
      data: $('#modify_user_form').serialize(),
      success: function(result) {
        if (result == 'no_change') {
          const message = 'No changes.';
          alertify.notify(message, 'warning', 5);
        } else if (result == 'success') {
          alertify.notify('User modified.', 'success', 5);
        } else {
          alertify.notify('There was an error', 'error', 5);
        }
      },
    });
  }
}

function add_user_form() { // eslint-disable-line no-unused-vars
  if ($('#add_user_form_submit').parsley().validate()) {
    $.ajax({
      type: 'POST',
      url: '/management/users/add_user',
      dataType: 'json',
      data: $('#modify_user_form').serialize(),
      success: function(result) {
        if (result == 'no_change') {
          const message = 'No changes.';
          alertify.notify(message, 'warning', 5);
        } else if (result == 'success') {
          alertify.notify('User modified.', 'success', 5);
        } else {
          alertify.notify('There was an error', 'error', 5);
        }
      },
    });
  }
}

function remove_user_form() { // eslint-disable-line no-unused-vars
  if ($('#modify_user_form').parsley().validate()) {
    $.ajax({
      type: 'POST',
      url: '/management/users/remove_user',
      dataType: 'json',
      data: $('#modify_user_form').serialize(),
      success: function(result) {
        if (result == 'no_change') {
          const message = 'No changes.';
          alertify.notify(message, 'warning', 5);
        } else if (result == 'success') {
          alertify.notify('User modified.', 'success', 5);
        } else {
          alertify.notify('There was an error', 'error', 5);
        }
      },
    });
  }
}