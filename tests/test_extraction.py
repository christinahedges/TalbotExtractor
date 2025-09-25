# Third-party
import numpy as np
from astropy.io import fits

# First-party/Local
from talbotextractor import PACKAGEDIR, Frame

# def test_load():
#     fname = f"{PACKAGEDIR}/data/test.fits"
#     mask = fits.open(f"{PACKAGEDIR}/data/mask.fits")[1].data.astype(bool)
#     te = TalbotExtractor(fname, ref_frame=1, pixel_mask=mask)
#     fig = te.plot_registration()
#     fig.savefig(
#         f"{DOCSDIR}/images/registration.png", dpi=150, bbox_inches="tight"
#     )
#     hdulist = te.extract_spots()
#     for attr in ["flux", "bkg", "flux_err"]:
#         y = hdulist[1].data[attr]
#         assert len(y) > 1000
#         assert np.isfinite(y).sum() > 1000


def test_load():
    data = fits.open(f"{PACKAGEDIR}/data/test.fits")[1].data[0]
    image = data[1].astype(float) - data[0].astype(float)
    mask = fits.open(f"{PACKAGEDIR}/data/mask.fits")[1].data.astype(bool)
    frame = Frame(image, pixel_mask=mask)
    assert (frame.A == np.eye(3)).all()
    frame._rough_position_calibration()
    assert not (frame.A != np.eye(3)).all()
    # fig = te.plot_registration()
    # fig.savefig(f"{DOCSDIR}/images/registration.png", dpi=150, bbox_inches="tight")
    # hdulist = te.extract_spots()
    # for attr in ["flux", "bkg", "flux_err"]:
    #     y = hdulist[1].data[attr]
    #     assert len(y) > 1000
    #     assert np.isfinite(y).sum() > 1000
