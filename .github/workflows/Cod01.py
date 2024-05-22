fx1 = 1412.00
per1 = 0.075
vlr1 = fx1 * per1
fx2 = 2666.68
per2 = 0.09
vlr2 = ((fx2 - fx1) * per2) + vlr1
fx3 = 4000.03
per3 = 0.12
vlr3 = ((fx3 - fx2) * per3) + vlr2
fx4 = 7786.02
per4 = 0.14
vlr4 = ((fx4 - fx3) * per4) + vlr3
valorcalc = 0
basecalc = float(input("Digite a base de cálculo do INSS: "))
if basecalc > fx4:
  valorcalc = vlr4
elif basecalc > fx3:
  valorcalc = ((basecalc - fx3) * per4) + vlr3
elif basecalc > fx2:
  valorcalc = ((basecalc - fx2) * per3) + vlr2
elif basecalc > fx1:
  valorcalc = ((basecalc - fx1) * per2) + vlr1
else:
  valorcalc = basecalc * per1
print ("O valor da base do INSS é: ", round(basecalc ,2))
print ("O valor do INSS calculado é: ", round(valorcalc ,2))

fxi0 = 2112.00
fxi1 = 2826.65
peri1 = 0.075
ded1 = 169.44
fxi2 = 3751.05
peri2 = 0.15
ded2 = 381.44
fxi3 = 4664.68
peri3 = 0.225
ded3 = 662.77
fxi4 = 99999999.99
peri4 = 0.275
ded4 = 896.00
vldep = 189.59
vlsimp = 528.00
cpdep = 0
vlrded = 0
vlrdesc = 0
qtdep = float(input("Digite a quantidade de dependentes para IR: "))
cpdep = qtdep * vldep

if (cpdep + valorcalc) < vlsimp:
  vlrded = vlsimp
else:
  vlrded = cpdep + valorcalc

basecalci = basecalc - vlrded

print ("O valor da base do IRRF é: ", round(basecalci ,2))
if basecalci < fxi0:
  vlrdesc = vlrdesc
elif basecalci < fxi1:
  if basecalci * peri1 - ded1 < 10.00:
    vlrdesc = vlrdesc
  else:
    vlrdesc = basecalci * peri1 - ded1
elif basecalci < fxi2:

  vlrdesc = basecalci * peri2 - ded2
elif basecalci < fxi3:
  vlrdesc = basecalci * peri3 - ded3
else:
  vlrdesc = basecalci * peri4 - ded4

print("O valor do Imposto de Renda é: ", round(vlrdesc ,2))
