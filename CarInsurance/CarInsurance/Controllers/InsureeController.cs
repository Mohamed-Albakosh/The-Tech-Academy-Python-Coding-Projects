using CarInsurance.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace CarInsurance.Controllers
{
    public class InsureeController : Controller
    {
     // public ActionResult Index()
      //  {
      //      return View();
      //  }
         //GET: Admin
        [HttpPost]
        public ActionResult Index(string firstName, string lastName, string emailAddress,DateTime dateOfBirth,int carYear, string carMake,
                                  string carModel,bool dUI,int speedingTickets, bool CoverageType,decimal quote)
        {
            

                using (InsuranceEntities db = new InsuranceEntities())
                {
                var insure = new Table();
                    insure.FirstName = firstName;
                    insure.LastName = lastName;
                    insure.EmailAddress = emailAddress;
                    insure.DateOfBirth = dateOfBirth;
                    insure.CarYear = carYear;
                    insure.CarMake = carMake;
                    insure.CarModel = carModel;
                    insure.DUI = dUI;
                    insure.SpeedingTickets = speedingTickets;
                    insure.CoverageType = CoverageType;
                    insure.Quote = quote;

                    db.Tables.Add(insure);
                    db.SaveChanges();
                }
            return View();
        }
                
    }
}