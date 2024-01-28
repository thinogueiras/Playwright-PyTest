def soma_valores(page):
    numb1 = int(page.locator("span[id='numb1']").text_content())
    numb2 = int(page.locator("span[id='numb2']").text_content())
    soma = numb1 + numb2

    return page.fill("input[id='number']", str(soma))


def dialog_validate(page, dialog_message):
    def on_dialog(dialog):
        assert dialog.message == dialog_message
        dialog.accept()

    return page.on('dialog', on_dialog)
