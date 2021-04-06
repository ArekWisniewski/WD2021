# Za pomocą wyrażenia generującego stwórz generator zwracający polskie nazwy miesięcy.

def miesiace():
    kalendarz=['styczen','luty','marzec','kwiecien','maj','czerwiec','lipiec','sierpien','wrzesien','pazdziernik','listopad','grudzien']
    for i in range (0,12):
        yield kalendarz[i]

rok=miesiace()
for i in range(0, 12):
    print(next(rok))