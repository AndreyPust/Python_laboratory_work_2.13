def replace_char(char_find, char_replace):
    """
    Функция производит замену последовательности искомых символов (char_find)
    на один указанный в переденных аргументах символ (char_replace).
    Для того, чтобы функции можно было передать новое предложение или строку
    при тех же искомых и меняемых символах, в функции используется замыкание,
    поэтому в дальнейшем, при вызове функции ей передается всего один аргумент
    - новое предложение для замены.
    В качестве результата функция возвращает то, что возвращает вложанная функция,
    а именно измененное предложение.
    """
    def in_func(proposal):
        result_proposal = ''
        prev_char = ''
        count = 0
        len_proposal = len(proposal)

        # Произведем замену последовательностей нужных символов.
        for char in proposal:
            if count == len_proposal - 1:
                break
            if char != char_find:
                result_proposal += char
            if char == char_find and char == prev_char and proposal[count + 1] != prev_char:
                result_proposal += char_replace

            prev_char = char
            count += 1
        return result_proposal

    return in_func
