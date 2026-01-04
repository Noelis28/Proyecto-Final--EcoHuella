# Importar
from flask import Flask, render_template, request


app = Flask(__name__)

def result_calculate(size, lights, device):
    # Variables que permiten calcular el consumo energético de los aparatos
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

# La primera página
@app.route('/')
def index():
    return render_template('index.html')


# Página de transporte
@app.route('/transporte')
def transporte():
    return render_template('transporte.html')


# Página de electricidad
@app.route('/electricidad')
def electricidad():
    return render_template('electricidad.html')


# Página de residuos
@app.route('/residuos')
def residuos():
    return render_template('residuos.html')

# Página de resultados de transporte
@app.route('/calcular_transporte', methods=['POST'])
def calcular_transporte():
    bicicleta = request.form.get('bicicleta')
    publico = request.form.get('publico')
    carro = request.form.get('carro')
    km = request.form.get('km')
    carpooling = request.form.get('carpooling')
    
    # Función para calcular impacto (bajo, medio, alto)
    def calcular_impacto_transporte(bici, pub, car, kms, carp):
        impacto = 0
        if bici == 'no': impacto += 1
        if pub == 'no': impacto += 1
        if car == 'si': impacto += 2
        if kms == 'medio': impacto += 1
        elif kms == 'alto': impacto += 2
        if carp == 'no': impacto += 1

        if impacto <= 2: return 'bajo'
        elif impacto <= 3: return 'medio'
        else: return 'alto'
    
    impacto = calcular_impacto_transporte(bicicleta, publico, carro, km, carpooling)
    return render_template('transporte_result.html', impacto=impacto)

# Página de resultados de electricidad
@app.route('/calcular_electricidad', methods=['POST'])
def calcular_electricidad():
    horas = request.form.get('horas')
    led = request.form.get('led')
    apagar = request.form.get('apagar')
    climatizacion = request.form.get('climatizacion')
    electro = request.form.get('electro')
    
    # Función para calcular impacto
    def calcular_impacto_electricidad(hor, led_val, apa, clim, elec):
        impacto = 0
        if hor == 'medio': impacto += 1
        elif hor == 'alto': impacto += 2
        if led_val == 'no': impacto += 1
        if apa == 'no': impacto += 1
        if clim == 'medio': impacto += 1
        elif clim == 'alto': impacto += 2
        if elec == 'medio': impacto += 1
        elif elec == 'alto': impacto += 2

        
        if impacto <= 2: return 'bajo'
        elif impacto <= 3: return 'medio'
        else: return 'alto'
    
    impacto = calcular_impacto_electricidad(horas, led, apagar, climatizacion, electro)
    return render_template('electricidad_result.html', impacto=impacto)

    
# Página de resultados de residuos
@app.route('/calcular_residuos', methods=['POST'])
def calcular_residuos():
    plastico = request.form.get('plastico')
    reciclar = request.form.get('reciclar')
    bolsas_reutilizables = request.form.get('bolsas_reutilizables')
    generar = request.form.get('generar')
    compostar = request.form.get('compostar')
    
    # Función para calcular impacto
    def calcular_impacto_residuos(pla, rec, emp, kg, uno):
        impacto = 0
        if pla == 'si': impacto += 1
        if rec == 'no': impacto += 1
        if emp == 'no': impacto += 1
        if kg == 'medio': impacto += 1
        elif kg == 'alto': impacto += 2
        if uno == 'si': impacto += 1  # Si 'si' significa que SÍ evita, pero ajusta lógica

        if impacto <= 2: return 'bajo'
        elif impacto <= 3: return 'medio'
        else: return 'alto'
    
    impacto = calcular_impacto_residuos(plastico, reciclar, bolsas_reutilizables, generar, compostar)
    return render_template('residuos_result.html', impacto=impacto)

# Página del Modo Educativo
@app.route('/modo_educativo')
def modo_educativo():
    return render_template('modo_educativo.html')
    
app.run(debug=True)  # inicia el servidor








