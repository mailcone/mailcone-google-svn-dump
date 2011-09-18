

ui_elements = {
  init_functions: ['splitter',
                   'accordion',
                   'tabs',
                   'elastic',
                   'datatable',
                   'buttons',
                   'add',
                   'form_controls'],
  
  
  init: function(context){
    ui_elements._form_controls_mapping();
    $.each(ui_elements.init_functions, function(index, func){
        ui_elements[func](context);
    });
  },
  
  
  accordion: function(context){
      var init = function(obj){
          var options = {};
          var data = obj.data('accordion-options');
          if (data)
            options = $.extend(options, data);
          obj.accordion(options);
      }
      ui_elements._context(context).find('.ui-accordion').each(function(){
          
          if($(this).hasClass('uldata')){
              var accordion = $(this);
              accordion.children().children().each(function(){
                  accordion.append('<h3>'+$(this).html()+'</h3>');
                  accordion.find('h3:last div:first').appendTo(accordion);
              });
              accordion.find('ul:first').remove();
              init($(this));
          }else {
              init($(this));
          }
      })
  },
  
  
  tabs: function(){
      $('.ui-tabs').each(function(){
          var options = {};
          var data = $(this).data('tabs-options');
          if (data)
            options = $.extend(options, data);
          $(this).tabs();
      });
  },
  
  
  elastic: function(){
      $('textarea').elastic();
  },
  
  
  datatable: function(context){
    ui_elements._context(context).find('.ui-datatable').each(function(){
         var table = $(this).dataTable( {
            sDom: 'T<"clear">frtiS',
            sScrollY: '200px',
            bDeferRender: true,
            bAutoWidth: false,
            sAjaxSource: $(this).data('ajaxurl'),
            bServerSide: true,
            bJQueryUI: true,
            fnDrawCallback: $.proxy(ui_elements._datatable_redraw, this),
            fnServerData: $.proxy(ui_elements._datatable_json, this),
            oTableTools: $(this).data('tabletools'),
        } );

        $(this).find('tbody').click(function(event) {
            var tr = $(event.target.parentNode);
            $(table.fnSettings().aoData).each(function (){
                $(this.nTr).removeClass('row_selected');
            });
            if (tr.data('ajaxcontent')){
                $(tr).addClass('row_selected');
                $('#ui-datatable-ajaxcontent').load(tr.data('ajaxcontent'));
            }
        });
    });
      
  },


  splitter: function(context){
    ui_elements._context(context).find('.ui-splitter').splitter({type: 'h', anchorToWindow:false,});
  },
  
  
  buttons: function(context){
      ui_elements._context(context).find( '.ui-button' ).each(function(){
          var option = { icons: {primary:$(this).data('ui-icon')},
                         text: $(this).data('ui-text')?$(this).data('ui-text'):false};
          $(this).button(option);
          
      });
  },
  
  
  add: function(context){
    ui_elements._context(context).find('.ui-add').each(function(){
        $(this).click(function(){
            ui_elements._ajax_modal($(this).attr('href'), $(this));
            return false;
        });
        
    });
  },
  
  
  _form_controls_mapping: function(){
    if (!ui_elements.form_controls_mapping)
     ui_elements.form_controls_mapping = {};
    ui_elements.form_controls_mapping['form.actions.submit']= ui_elements._form_controls_submit;
    ui_elements.form_controls_mapping['form.actions.add']= ui_elements._form_controls_submit;
    ui_elements.form_controls_mapping['form.actions.edit']= ui_elements._form_controls_submit;
    ui_elements.form_controls_mapping['form.actions.delete']= ui_elements._form_controls_submit;
    ui_elements.form_controls_mapping['form.actions.cancel']= ui_elements._form_controls_cancel;
    
  },


  form_controls: function(){
      var dialog = $('#ui-modal-content');
      var form = $('.actionsView').parents('form');
      form.submit(function(){
          return false;
      });
      var buttons = {};
      form.find('input[type="submit"]').each(function(){
          if ($(this).attr('id') in ui_elements.form_controls_mapping){
              var func = ui_elements.form_controls_mapping[$(this).attr('id')];
              buttons[$(this).val()] = $.proxy(func, this);
          }
      });
      dialog.dialog('option', 'buttons', buttons);
      dialog.find('.actionsView input').remove();

  },
  
  _context: function(context){
      if (context instanceof $)
        return context;
      return $('html');
      
  },
  
  
  _datatable_redraw: function(){
      $(this).find('tr .ui-datatable-ajaxlink').click(function(){
          ui_elements._ajax_modal($(this).attr('href'), $(this));
          return false;
      });
  },
  
  
  _datatable_json: function(sSource, aoData, fnCallback){
      var table = $(this)
      $.getJSON( sSource, aoData, function (json) {
          fnCallback(json);
          if (!json.metadata)
            return;
          var metadata = json.metadata;
          if (metadata.ajaxcontent) {
              table.find('tr').each(function(index){
                  $(this).data('ajaxcontent', metadata.ajaxcontent[index-1]);
              });
          }
      });
  },
  
  
  _ajax_modal: function(url, element, postdata, callback){
      var dialogid = 'ui-modal-content';
      if (!$('#'+dialogid).length)
        $('body').append('<div id="'+dialogid+'"/>');
      var dialog = $('#'+dialogid);
      dialog.load(url, postdata, function(){
          ui_elements._init_dialog(dialog, element);
          if (callback)
            callback(dialog);
      });
    },
  
  
  _init_dialog: function(dialog, element){
      dialog.dialog({height: element?element.hasClass('ui-modal-minsize')?200:600:600,
                     width: 500,
                     modal: true});
      var title = dialog.find('h1:first');
      dialog.dialog( 'option', 'title', title.html() );
      title.remove();
      ui_elements.init(dialog);
  },
  
  _form_controls_submit: function(){
        var dialog = $('#ui-modal-content');
        var form = $('.actionsView').parents('form');
        var additional = '&'+$(this).attr('name')+'='+$(this).val();
        dialog.load(form.attr('action'),form.serialize() + additional, function(){
            if (dialog.find('.error').length)
               ui_elements._init_dialog(dialog);
            else
               window.location.reload(true);
        });
      },
      
      
  _form_controls_cancel: function(){
        var dialog = $('#ui-modal-content');
        dialog.dialog('close');
        return false;
      },
  
  
}
jQuery(document).ready(ui_elements.init);
