from Console.GUI import GUI
from Console.UI import UI
from Settings.settings import Settings
from Strategy.ConcreteStrategyA import ConcreteStrategyA
from Strategy.ConcreteStrategyB import ConcreteStrategyB
from Strategy.ConcreteStrategyC import ConcreteStrategyC

from Strategy.Strategy import Context

settings = Settings()


if settings.strategy == 'A':
    context = Context(ConcreteStrategyA())
elif settings.strategy == 'B':
    context = Context(ConcreteStrategyB())
else:
    context = Context(ConcreteStrategyC())

if settings.ui == 'UI':
    ui = UI(context)
else:
    ui = GUI(context)

ui.start()
