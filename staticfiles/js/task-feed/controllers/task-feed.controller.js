/**
* TaskFeedController
* @namespace crowdsource.task-feed.controllers
 * @author dmorina
*/
(function () {
  'use strict';

  angular
    .module('crowdsource.task-feed.controllers')
    .controller('TaskFeedController', TaskFeedController);

  TaskFeedController.$inject = ['$window', '$location', '$scope', 'TaskFeed', '$filter', 'Authentication'];

  /**
  * @namespace TaskFeedController
  */
  function TaskFeedController($window, $location, $scope, TaskFeed, $filter, Authentication) {
      var userAccount = Authentication.getAuthenticatedAccount();
      if (!userAccount || !userAccount.profile) {
        $location.path('/login');
        return;
      }
      
      var self = this;
      self.toggleBookmark = toggleBookmark;
      self.modules = [];

      TaskFeed.getProjects().then(
        function success (successData) {
          var data = successData[0];
        },
        function error(errData) {
          self.error = errData[0].detail;
        }
      ).finally(function () {
        self.modules.push({"id": 1, "milestoneDescription": "this is a milestone description", "payment":{"number_of_hits":"10","total":"6.00","wage_per_hit":"0.5","charges":"1"},"selectedCategories":[0,3,4],"name":"Sample project 1","description":"This is my sample description","taskType":"oneTask","upload":"noFile","onetaskTime":"1 hour","template":{"name":"template_bMuDT98e","items":[{"id":"id1","name":"label","type":"label","width":100,"height":100,"values":"Enter Name","role":"display","sub_type":"h4","layout":"column","icon":null,"data_source":null},{"id":"id2","name":"text_field_placeholder","type":"text_field","width":100,"height":100,"values":null,"role":"display","sub_type":null,"layout":"column","data_source":null},{"id":"id3","name":"label","type":"label","width":100,"height":100,"values":"Enter Place of Birth","role":"display","sub_type":"h4","layout":"column","icon":null,"data_source":null},{"id":"id4","name":"text_field_placeholder","type":"text_field","width":100,"height":100,"values":null,"role":"display","sub_type":null,"layout":"column","data_source":null},{"id":"id5","name":"label","type":"label","width":100,"height":100,"values":"Favorite Quote","role":"display","sub_type":"h4","layout":"column","icon":null,"data_source":null},{"id":"id6","name":"text_area_placeholder","type":"text_area","width":100,"height":100,"values":null,"role":"display","sub_type":null,"layout":"column","data_source":null}]}});
      });
       
      
      self.modules = [
          // {
          //     id: 1,
          //     name: "Build a website using AngularJs",
          //     description: "Build a website using Python Django Framework, AngularJs and Material Design",
          //     category: "Programming",
          //     skills: "html, angularjs, python, django, css",
          //     tasks: 32,
          //     requester: 'neilg',
          //     time_to_complete: '2 days',
          //     is_bookmarked: true,
          //     pay: '$150'


          // },
          // {
          //     id: 2,
          //     name: "Help me write a research paper",
          //     description: "Topic of the paper is crowd sourcing platforms...",
          //     tasks: 23,
          //     category: "Writing",
          //     skills: "English, research",
          //     requester: 'dmorina',
          //     time_to_complete: '10 days',
          //     is_bookmarked: false,
          //     pay: '$256'
          // },
          // {
          //     id: 3,
          //     name: "Take my dire wolf for a walk",
          //     description: "A short walk around Winterfell",
          //     tasks: 13,
          //     category: "Reading",
          //     skills: "Walking, Dire wolf language",
          //     requester: 'jon.snow',
          //     time_to_complete: '4 hours',
          //     is_bookmarked: true,
          //     pay: '$20'
          // },
      ];
      function toggleBookmark(project){
          project.is_bookmarked = !project.is_bookmarked;
      }
  }

})();