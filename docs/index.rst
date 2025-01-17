===========================================
Welcome to django-portlets's documentation!
===========================================

What is it?
===========

Portlets are pieces of content which are managed in Slots. Slots can be freely
defined and placed anywhere within a HTML page.

django-portlets provides just a generic engine to manage portlets. You can find
a comprehensive implementation within `LFS`_.

Installation
============

To install just do:

1. ``python setup.py install`` or ``pip install django-portlets``

2. Add portlets to ``INSTALLED_APPS``.

Usage
=====

In order to use django-portlets you first have to implement a portlet. This is
done by inheriting from the provided base class, for instance:

**Create a portlet**

Let's create a simple text portlet::

    # django imports
    from django import forms
    from django.db import models
    from django.template.loader import render_to_string
    from django.utils.translation import ugettext_lazy as _

    from portlets.models import Portlet

    class TextPortlet(Portlet):
        """A simple portlet to display some text.
        """
        text = models.TextField(_(u"Text"), blank=True)

        def __str__(self):
            return "%s" % self.id

        def render(self, context):
            """Renders the portlet as html.
            """
            return render_to_string("portlets/text_portlet.html", {
                "title" : self.title,
                "text" : self.text
            })

        def form(self, **kwargs):
            """
            """
            return TextPortletForm(instance=self, **kwargs)

    class TextPortletForm(forms.ModelForm):
        """Form for the TextPortlet.
        """
        class Meta:
            model = TextPortlet

**Create the template**

To display the content of the portlet we will have to create a simple template in this case text_portlet.html. It can look like this::

    <div class="portlet">
        <div class="portlet-header">
            {{ title }}
        </div>
        <div class="portlet-body">
            {{ text|safe }}
        </div>
    </div>

**Register the portlet**

In order to make it available for selection, the portlet has to be registered
(make sure that this is called, when django starts up)::

    from portlets.utils import register_portlet
    register_portlet(TextPortlet, "TextPortlet")

To display portlets within your templates, just use the provided portlet_slot
tag, e.g.::

   {% load portlets_tags %}

   <table>
        <tr>
            <td>
                {% portlet_slot 'Left' flatpage %}
            </td>
            <td>
                Content goes here.
            </td>
            <td>
                {% portlet_slot 'Right' flatpage %}
            </td>
        </tr>
   </table>

Example
=======

django-portlets provides a simple example with a complete implementation of a portlet. Please refer to it if you wan to write your own portlets.

**Installation of the example**

1. Install `flatpages`_ (flatpages serve as our example content)

2. Add the portlets and portlets.example to INSTALLED_APPS

3. Sync the database

    $ bin/django syncdb

4. Go to django admin and:

    1. add a flatpage

    2. add a TextPortlet

    3. assign the TextPortlet to the flatpage (via PortletAssignment)

5. Browse to the flatpage

Indices and tables
==================

* :ref:`search`

.. _LFS: http://bitbucket.org/diefenbach/django-lfs
.. _LFC: http://bitbucket.org/diefenbach/django-lfc
.. _`flatpages`: http://docs.djangoproject.com/en/dev/ref/contrib/flatpages/
