opcao, qtd = map(int, input().split())

match opcao:
    case 1:
        total = qtd * 4.0
        print(f'Total: R$ {total:.2f}')
    case 2:
        total = qtd * 4.5
        print(f'Total: R$ {total:.2f}')
    case 3:
        total = qtd * 5.0
        print(f'Total: R$ {total:.2f}')
    case 4:
        total = qtd * 2.0
        print(f'Total: R$ {total:.2f}')
    case 5:
        total = qtd * 1.5
        print(f'Total: R$ {total:.2f}')
