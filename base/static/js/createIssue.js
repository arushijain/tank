 $(function() {
            $(".inline.{{ sublocation_form.prefix }}").formset({
                prefix: "{{ sublocation_form.prefix }}",
            })
            $(".inline.{{ user_form.prefix }}").formset({
                prefix: "{{ user_form.prefix }}",
            })
        })