# -*- coding:utf8 -*-
from abc import ABCMeta, abstractmethod


class Director(object, metaclass=ABCMeta):
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self._builder = builder

    @abstractmethod
    def construct(self, field_list):
        pass

    def get_constructed_object(self):
        return self._builder.constructed_object


class FormDirecotr(Director):
    def __init__(self):
        Director.__init__(self)

    def construct(self, field_list):
        for field in field_list:
            if field['field_type'] == 'text_field':
                self._builder.add_text_field(field)
            elif field['field_type'] == 'checkbox':
                self._builder.add_checkbox(field)
            elif field['field_type'] == 'button':
                self._builder.add_button(field)


class AbstractFormBuilder(object, metaclass=ABCMeta):
    def __init__(self):
        self.constructed_object = None

    @abstractmethod
    def add_text_field(self, field_dict):
        pass

    @abstractmethod
    def add_checkbox(self, checkbox_dict):
        pass

    @abstractmethod
    def add_button(self, button_dict):
        pass


class HtmlForm(object):
    def __init__(self):
        self.field_list = []

    def __repr__(self):
        return '<form>{}</form>'.format(''.join(self.field_list))


class HtmlFormBuilder(AbstractFormBuilder):
    def __init__(self):
        self.constructed_object = HtmlForm()

    def add_text_field(self, field_dict):
        self.constructed_object.field_list.append(
            '{0}:<br><input type="text" name="{1}"><br>'.format(field_dict['label'], field_dict['field_name'])
        )

    def add_checkbox(self, checkbox_dict):
        self.constructed_object.field_list.append(
            '<label><input type="checkbox" id="{0}" value="{1}"></label>{2}<br>'.format(checkbox_dict['field_id'], checkbox_dict['value'], checkbox_dict['label'])
        )

    def add_button(self, button_dict):
        self.constructed_object.field_list.append(
            '<button type="button">{}</button>'.format(button_dict['text'])
        )


if __name__ == '__main__':
    director = FormDirecotr()
    builder = HtmlFormBuilder()

    director.set_builder(builder)
    field_list = [
        {
            'field_type': 'text_field',
            'label': 'best text you have ever written',
            'field_name': 'field one'
        },
        {
            'field_type': 'checkbox',
            'field_id': 'check_it',
            'value': '1',
            'label': 'check for on'
        },
        {
            'field_type': 'text_field',
            'label': 'another text field',
            'field_name': 'field one'
        },
        {
            'field_type': 'button',
            'text': 'DONE'
        }
    ]
    director.construct(field_list)

    with open('form_builder.html', 'w') as f:
        f.write(
            '<html><body>{0!r}</body></html>'.format(director.get_constructed_object())
        )







