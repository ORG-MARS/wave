# Stat / Series / Tall / Interval
# Create a tall stat card displaying a primary value, an auxiliary value and a series plot.
# ---
import time

from faker import Faker

from synth import FakeCategoricalSeries
from h2o_wave import site, ui, data

page = site['/demo']

fake = Faker()
f = FakeCategoricalSeries()
cat, val, pc = f.next()
c = page.add(f'example', ui.tall_series_stat_card(
    box='1 1 1 2',
    title=fake.cryptocurrency_name(),
    value='=${{intl qux minimum_fraction_digits=2 maximum_fraction_digits=2}}',
    aux_value='={{intl quux style="percent" minimum_fraction_digits=1 maximum_fraction_digits=1}}',
    data=dict(qux=val, quux=pc / 100),
    plot_category='foo',
    plot_type='interval',
    plot_value='qux',
    plot_color='$red',
    plot_data=data('foo qux', -20),
    plot_zero_value=0,
))
page.save()

while True:
    time.sleep(1)
    cat, val, pc = f.next()
    c.data.qux = val
    c.data.quux = pc / 100
    c.plot_data[-1] = [cat, val]
    page.save()
